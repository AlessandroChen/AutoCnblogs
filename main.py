import xmlrpc.client as xmlrpclib
import json

config_path = "./blog_config.json"

def have_configed():
    '''
    return bool value : whether config file exists
    '''
    try:
        with open(config_path, "r", encoding = "utf-8") as f:
            try:
                cfg = json.load(f)
                return cfg == {}
            except json.decoder.JSONDecodeError:
                return False
    except:
        with open(config_path, "w", encoding = "utf-8") as f:
            json.dump({}, f)
            return False

if __name__ == "__main__":
    if have_configed() == False:
        pass
