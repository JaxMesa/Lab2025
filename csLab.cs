if (fileExtension == ".json")
{
    var jsonData = File.ReadAllText(C:\Users\nikit\OneDrive\Desktop\Lab\data.json);
    var jsonObject = JsonConvert.DeserializeObject<Dictionary<string, object>>(jsonData);
    // Process jsonObject as needed
}

foreach (var key in jsonObject.Keys)
{
    Console.WriteLine($"{key}: {jsonObject[key]}");
}