
import json
import jsonpath

def main():
    # Load JSON log file
    with open("rawlogs.txt", "r") as file:
        log_data = json.load(file)
        
        # Define JSONPath query (e.g., get all messages of ERROR level logs)
        jsonpath_expr = "$.[?match(@.type, 'apdu')]"

        path = jsonpath.compile(jsonpath_expr)
        # Execute query
        matches = path.findall(log_data)
        
        # Print results
        print(json.dumps(matches, indent=2))    


if __name__ == "__main__":
    main()