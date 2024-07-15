$exclude = @("venv", "bot-autonauts-of.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot-autonauts-of.zip" -Force