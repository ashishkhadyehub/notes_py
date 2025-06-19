from rich.console import Console
from rich.table import Table

# Create a console object
console = Console()

# Create a table
table = Table(title="Top Python Libraries")

# Add columns
table.add_column("Library", justify="left", style="cyan", no_wrap=True)
table.add_column("Use Case", style="magenta")
table.add_column("Popularity", justify="right", style="green")

# Add rows
table.add_row("NumPy", "Numerical Computing", "★★★★★")
table.add_row("Pandas", "Data Analysis", "★★★★★")
table.add_row("Rich", "Terminal Output Formatting", "★★★★☆")
table.add_row("Requests", "HTTP for Humans", "★★★★☆")

# Print the table
console.print(table)
