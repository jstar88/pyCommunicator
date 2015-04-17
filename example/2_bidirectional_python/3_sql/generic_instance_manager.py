from pyCommunicator.BackEndJsonCallback import BackEndJsonCallback

bjc = BackEndJsonCallback()
claz_objs = {}

def myHandler(data):
    global claz_objs
    idc = data['module']+data['class']+str(data['instance_args'])
    if idc in claz_objs:
        claz_obj = claz_objs[idc]
    else:
        module = __import__(data['module'])
        claz = getattr(module,data['class'])
        instance_args =data['instance_args']  
        claz_obj = claz(*instance_args)
        claz_objs[idc] = claz_obj
    
    methodToCall = getattr(claz_obj,data['method'])  
    bjc.write(methodToCall(*data['args']))
    

bjc.onRead += myHandler
bjc.run()