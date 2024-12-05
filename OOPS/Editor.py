
class Editor:
    def __init__(self,name,vendor):
        self.name=name
        self.vendor=vendor

    def __str__(self):
        return self.name
    

editor_instance1=Editor("Pycharm","Jetbrains")
editor_instanc2=Editor("VS Code","Microsoft")
editor_instance3=Editor("Anaconda","Python")
print(editor_instance1)
print(editor_instanc2)