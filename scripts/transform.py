def transform(data):
    return {
        "city": data["location"]["name"],
        "country": data["location"]["country"],
        "temperature": data["current"]["temperature"],
        "humidity": data["current"]["humidity"],
        "timestamp": data["location"]["localtime"]
    }
