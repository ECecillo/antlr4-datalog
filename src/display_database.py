from collections import defaultdict

def print_database(visitor):
        # Step 1: Organize data into a structured format
    structured_data = defaultdict(list)
    for fact in visitor.database:
        # Assuming the fact is in the format `predicate_name(column1, column2, ...)`
        # Extract predicate name and columns
        predicate_name = fact.predicate
        columns = fact.values
        structured_data[predicate_name].append(columns)

# Step 2: Determine the maximum length of each column
    max_lengths = {}
    for predicate_name, rows in structured_data.items():
        max_lengths[predicate_name] = [0] * len(rows[0])
        for row in rows:
            for idx, col in enumerate(row):
                max_lengths[predicate_name][idx] = max(max_lengths[predicate_name][idx], len(str(col)))

# Step 3: Print the data in a tabular format
    for predicate_name, rows in structured_data.items():
        print(f"\n{predicate_name.upper()}")
        
        # Print header
        header = ""
        for idx, max_length in enumerate(max_lengths[predicate_name]):
            col_name = f"column{idx + 1}"
            header += f"| {col_name.ljust(max_length + 2)}"
        header += "|"
        print(header)
        
        # Print separator
        separator = ""
        for max_length in max_lengths[predicate_name]:
            separator += "|" + "-" * (max_length + 3)
        separator += "|"
        print(separator)
        
        # Print rows
        for row in rows:
            row_str = ""
            for idx, col in enumerate(row):
                row_str += f"| {str(col).ljust(max_lengths[predicate_name][idx] + 2)}"
            row_str += "|"
            print(row_str)
