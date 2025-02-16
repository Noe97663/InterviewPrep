# Get the current directory (the folder where the script is running)
$currentDir = Get-Location

# Initialize a sum variable
$sum = 0

# Loop through each subfolder in the current directory
Get-ChildItem -Path $currentDir -Directory | ForEach-Object {
    # Use regex to match digits inside parentheses in the folder name
    if ($_.Name -match '\((\d+)\)') {
        # Convert the captured number to an integer and add to sum
        $num = [int]$matches[1]
        $sum += $num
        
        # Count the number of files in the folder (only files, not subdirectories)
        $filesCount = (Get-ChildItem -Path $_.FullName -File).Count
        
        # Based on your example, if the folder name is like "cars(3)", then it must contain 3+1 = 4 files.
        $expectedCount = $num + 1
        
        if ($filesCount -ne $expectedCount) {
            Write-Output "Folder '$($_.Name)' does not have the expected $expectedCount files (found $filesCount)."
        }
    }
}

# Output the total sum
Write-Output "Total sum: $sum"
