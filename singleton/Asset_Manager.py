# Singleton Class
# Singleton Pattern involves restricting a class to only a single instatiation
class Asset_Manager:
    _shared_state = {}

    # Override __new__ to only allow single instantiation
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance=super(Asset_Manager,cls).__new__(cls)
        return cls.instance
        

am1 = Asset_Manager()
am2 = Asset_Manager()
print(am1)
print(am2)
    