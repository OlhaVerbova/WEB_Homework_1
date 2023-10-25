#HomeWork_1

#Abstract class
class ShowInformation():
    def show_all_information(self):
        raise NotImplementedError #required function
    
class Show_to_console(ShowInformation):
    def show_all_information(self, response): 
        print(response)            
    
    def show_Error_Command(self):
        print("Unknown command. Type 'helper' for a list of available commands.")
    
    def greating_Message(self):
        print("Welcome to ContactBot!")
    
    def saved_Infornation_AddressBook(self, filename, address_book):
        print(f"Address book loaded from {filename}. {len(address_book.data)} contacts found.")