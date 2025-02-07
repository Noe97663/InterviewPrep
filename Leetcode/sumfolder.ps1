# Get the current directory (the folder where the script is running)
$currentDir = Get-Location

# Initialize a sum variable
$sum = 0

# Loop through each subfolder in the current directory
Get-ChildItem -Path $currentDir -Directory | ForEach-Object {
    # Use regex to match digits inside parentheses in the folder name
    if ($_.Name -match '\((\d+)\)') {
        # Convert the captured number (stored in $matches[1]) to an integer and add to sum
        $sum += [int]$matches[1]
    }
}

# Output the total sum
Write-Output "Total sum: $sum"
