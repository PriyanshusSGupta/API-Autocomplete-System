import requests
import time
from collections import deque

class AutocompleteExtractor:
    def __init__(self, base_url, version):
        self.base_url = base_url
        self.version = version
        self.visited = set()
        self.queue = deque()
        self.names = set()
        self.total_requests = 0

    def fetch_completions(self, prefix):
        url = f"{self.base_url}/{self.version}/autocomplete?query={prefix}"
        try:
            response = requests.get(url)
            self.total_requests += 1
            if response.status_code == 200:
                return response.json().get('results', [])
            else:
                print(f"Error fetching {prefix} from {self.version}: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error fetching {prefix} from {self.version}: {str(e)}")
            return []

    def extract_all_names(self):
        # Initialize with a-z
        for c in 'abcdefghijklmnopqrstuvwxyz':
            self.queue.append(c)
            self.visited.add(c)

        while self.queue:
            prefix = self.queue.popleft()
            completions = self.fetch_completions(prefix)
            time.sleep(0.1)

            for name in completions:
                if name not in self.names:
                    self.names.add(name)
                    if len(name) > len(prefix):
                        next_prefix = name[:len(prefix)+1]
                        if next_prefix not in self.visited:
                            self.visited.add(next_prefix)
                            self.queue.append(next_prefix)

        return sorted(self.names)


if __name__ == "__main__":
    base_url = "http://35.200.185.69:8000"
    versions = ["v1", "v2", "v3"]
    all_results = {}

    for version in versions:
        print(f"Extracting names from {version}...")
        extractor = AutocompleteExtractor(base_url, version)
        names = extractor.extract_all_names()
        
        all_results[version] = {
            "names": names,
            "total_requests": extractor.total_requests,
            "total_names": len(names),
        }

        print(f"Finished extracting from {version}:")
        print(f"Total names found: {len(names)}")
        print(f"Total API requests made: {extractor.total_requests}")
    
    # Summary of results across all versions
    print("\nSummary:")
    for version, data in all_results.items():
        print(f"{version.upper()}:")
        print(f"- Total Names: {data['total_names']}")
        print(f"- Total Requests: {data['total_requests']}")
