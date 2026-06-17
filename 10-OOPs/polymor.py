class Notification:
    def __init__(self, expediteur, destinataire):
        self._expediteur = expediteur
        self._destinataire = destinataire
    
    def envoyer(self, message):
        print(f"Envoi de {self._expediteur} à {self._destinataire} : {message}")

class NotificationCryptee(Notification):
    #def __init__(self, expediteur, destinataire):
        #super().__init__(expediteur, destinataire)
    
    def envoyer(self, message):
        message_crypter = message[::-1]
        super().envoyer(message_crypter)


send = NotificationCryptee("Alice", "Rob")
send.envoyer("Hello from the Beach")