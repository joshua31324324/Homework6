from abc import ABC, abstractmethod

#define command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
