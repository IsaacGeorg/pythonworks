
from abc import ABC,abstractmethod

class Editor(ABC):
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def write(self):
        pass
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def debug(self):
        pass
    @abstractmethod
    def file_creation(self):
        pass
    @abstractmethod
    def folder_creation(self):
        pass

class MS_Office(Editor):
    def open(self):
        print("Opening")

    def write(self):
        print("write")

    def execute(self):
        print("Executing")

    def debug(self):
        print("Debugging")

    def file_creation(self):
        print("Created_file")
    
    def folder_creation(self):
        print("Folder_created")


ms_instance=MS_Office()
ms_instance.execute()
ms_instance.debug()