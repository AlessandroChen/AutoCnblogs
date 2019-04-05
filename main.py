import xmlrpc.client as xmlrpclib
import json

config_path = "./blog_config.json"

def have_config():
    '''
    return bool value : whether config file exists
    '''
    try:
        with open(config_path, "r", encoding = "utf-8") as f:
            try:
                cfg = json.load(f)
                return cfg != {}
            except json.decoder.JSONDecodeError:
                return False
    except:
        with open(config_path, "w", encoding = "utf-8") as f:
            json.dump({}, f)
            return False

def create_config():
    '''
    create config file if it doesnt exist
    only save ensured data usr provided, if not print ERROR
    '''
    # Provide EXAMPLE Here

    for test_times in range(0, 2):
        cfg = {}
        for item in [("url", "metaWeblog url"),
                     ("appkey", "blogaddress"),
                     ("usr", "usrname"),
                     ("passwd", "password")]:
            cfg[item[0]] = input(item[1] + " : ")
        
        try:
            server = xmlrpclib.ServerProxy(cfg["url"])
            userInfo = server.blogger.getUsersBlogs(
                    cfg["appkey"], cfg["usr"], cfg["passwd"])
            print (userInfo[0])
            cfg["bolgid"] = userInfo[0]["blogid"]
            break
        except:
            print ("ERROR!!!")
            print ("Please Check It Again")
    with open(config_path, "w", encoding = "utf-8") as f:
        json.dump(cfg, f, indent = 4, ensure_ascii = False)


if __name__ == "__main__":
    if have_config() == False:
        create_config()
    print ("End")
