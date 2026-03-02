#38. Abstract Notification

from abc import ABC, abstractmethod

class Notification(ABC):
  @abstractmethod
  def notify(self):
    pass

class EmailNotification(Notification):
   def notify(self):
       print("Notified via Email")

n = EmailNotification()
n.notify()