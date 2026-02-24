import json
import unittest
from collections import Counter
import tldextract
import re

class TestTrackingProtectionLists(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('entities.json', 'r') as f:
            cls.entities_data = json.load(f)
        
        with open('services.json', 'r') as f:
            cls.services_data = json.load(f)

        cls.entities = cls.entities_data["entities"]
        cls.services = cls.services_data["categories"]
        cls.tld_extract = tldextract.TLDExtract(suffix_list_urls=())

    def test_validate_json(self):
        """Test if the JSON data is valid and can be loaded."""
        self.assertIsInstance(self.entities_data, dict)
        self.assertIsInstance(self.services_data, dict)

    def test_entities_exist_in_services(self):
        """Ensure all entities listed in services.json exist in the entities.json list."""
        entities_in_services = {entity for service_entries in self.services.values()
                                       for entry in service_entries
                                       for entity in entry}
        
        entities_in_entities = set(self.entities.keys())
        
        missing_entities = entities_in_services - entities_in_entities
        self.assertEqual(len(missing_entities), 0, f"Missing entities: {missing_entities}")

    def test_no_duplicate_domains_across_entities(self):
        """Ensure there are no duplicate domains across different entities."""
        all_domains = set()

        for entity_name, entity_data in self.entities.items():
            domains = set(entity_data.get('properties', [])) | set(entity_data.get('resources', []))
            
            duplicate_domains = all_domains & domains

            self.assertEqual(len(duplicate_domains), 0, f"Duplicate domains found in entity {entity_name}: {duplicate_domains}")

            all_domains.update(domains)
    
    def test_no_duplicate_entities(self):
        """Ensure there are no duplicate entities with the same name."""
        entity_names = [name for name in self.entities.keys()]
        unique_entity_names = set(entity_names)

        self.assertEqual(len(entity_names), len(unique_entity_names), 
                         "Duplicate entity names found in the entities list.")
        
    def test_no_duplicate_entities_in_same_category(self):
        """Ensure there are no duplicate entities in the same category in services.json."""
        for category, services in self.services.items():
            all_entities_in_category = []
            for service in services:
                all_entities_in_category.extend(service.keys())

            entity_counts = Counter(all_entities_in_category)
            duplicates = [entity for entity, count in entity_counts.items() if count > 1]

            self.assertEqual(len(duplicates), 0, 
                             f"Duplicate entities found in category '{category}': {duplicates}")
            
    def test_services_root_domains_exist_in_entities(self):
        """Ensure every root domain in services.json is present in the properties or resources of entities.json."""
        # Collect all root domains (extracted from domains) from services.json
        services_root_domains = set()
        for category_data in self.services.values():
            for entry in category_data:
                for entity, urls in entry.items():
                    for url, domains in urls.items():
                        if isinstance(domains, list):
                            for domain in domains:
                                extracted = self.tld_extract(domain)
                                root_domain = "{}.{}".format(extracted.domain, extracted.suffix)
                                services_root_domains.add(root_domain)

        # Collect all domains from entities.json
        entities_domains = set()
        for entity_data in self.entities.values():
            entities_domains.update(entity_data.get('properties', []))
            entities_domains.update(entity_data.get('resources', []))

        # Extract root domains from entities domains
        entities_root_domains = set()
        for domain in entities_domains:
            extracted = self.tld_extract(domain)
            root_domain = "{}.{}".format(extracted.domain, extracted.suffix)
            entities_root_domains.add(root_domain)

        # Check if each root domain from services.json exists in entities.json
        missing_root_domains = services_root_domains - entities_root_domains
        self.assertEqual(len(missing_root_domains), 0, 
                        f"Root domains in services.json not found in entities.json: {missing_root_domains}")
        
    def test_validate_domain_formats(self):
        """Ensure all domains are in a valid format."""
        # Regular expression for a simple domain validation
        domain_regex = re.compile(r'^[^@]+\.[^@]+$')
        
        # Validate entities domains
        for entity_data in self.entities.values():
            for domain_type in ['properties', 'resources']:
                for domain in entity_data.get(domain_type, []):
                    self.assertRegex(domain, domain_regex, f"Invalid domain in entities: {domain}")

        # Validate services domains
        for category_data in self.services.values():
            for entry in category_data:
                for entity_data in entry.values():
                    for url, domains in entity_data.items():
                        if isinstance(domains, list):
                            for domain in domains:
                                self.assertRegex(domain, domain_regex, f"Invalid domain in services: {domain}")
    
    def test_no_duplicate_domains_within_same_entity(self):
        """Ensure there are no duplicate domains within the same entity's properties or resources."""
        for entity_name, entity_data in self.entities.items():
            properties = entity_data.get('properties', [])
            resources = entity_data.get('resources', [])
            
            # Check for duplicates within properties
            properties_counts = Counter(properties)
            properties_duplicates = [domain for domain, count in properties_counts.items() if count > 1]
            
            self.assertEqual(len(properties_duplicates), 0, 
                           f"Duplicate domains found in properties of entity '{entity_name}': {properties_duplicates}")
            
            # Check for duplicates within resources
            resources_counts = Counter(resources)
            resources_duplicates = [domain for domain, count in resources_counts.items() if count > 1]
            
            self.assertEqual(len(resources_duplicates), 0, 
                           f"Duplicate domains found in resources of entity '{entity_name}': {resources_duplicates}")

if __name__ == "__main__":
    unittest.main()
