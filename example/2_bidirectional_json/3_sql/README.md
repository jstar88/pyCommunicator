## sql example

Let's suppose that our main environment is built without splite3 support:  
this example show you how solve the problem using an external python environment with sqlite3 enabled.   
As always, we call *service* the external tool and the relative folder contains all what it needs.  
Just to make more realistic the example, the service is built in a .exe with py_installer module but it could be also a .py file running in a portable python version.  
  

### Archetype

1.  **main.py** : it's the root thread and it do some DB operations printing the results
2.  **DBStub.py** : it contains a list of useful methods for our purpose and emulate the database sending a dictionary of useful informations to the *generic_instance_manager.py* through the *FrontEndJsonCallback* object. The dictionary keys are:
   * module : the module containing the target class , in our case *Database*
   * class : the target class, in our case *Database*
   * instance_args : a list of constructor's arguments, in our case *[dbname]*
   * method: the method to call,  in our case are the methods of class *Database.py*
   * args: a list of method's arguments, in our case most of time is *[query,(values)]*
3. **generic_instance_manager.py**: this class take the dictionary as above,create the relative object and call the method.  
It's important to say that it use the *multitone* pattern, so it check for instanced class with the right arguments and return it. If not exist then it will be created and saved.  
In this way you can use multiple instances of same class at same time, each one with different construct args.  
In our case, we can use multiple *Database* instances but they must have different name, of course.  
This manager is pretty cool since it can be used for different purposes and services.  

4.**Database.py**: Finally, it is the pure database implementation, more generic as possible for large usage.  
5. **imports.py**: It's used to "show" to pyInstaller the hidden imports.  
6.**compile.bat**: contains the cmd command to compile generic_instance_manager.py to .exe using pyInstaller module.  
7. **other folders**: the pyCommunicator is included both in main thread and in the service, since it's supposed to be external.  *dist* contains the compiled generic_instance_manager.exe