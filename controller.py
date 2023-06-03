import view
import model
import text
#делаем функцию старт

def start():

    my_pb = model.PhoneBook()
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                my_pb.open()
                view.print_message(text.load_successful)
            case 2:
                my_pb.save()
                view.print_message(text.save_successful)
            case 3:
                pb = my_pb.load()
                view.print_contact(pb, text.load_error)
            case 4:
                contact = view.input_contact(text.new_contact, text.cancel_input)
                name = my_pb.add(contact)
                view.print_message(text.new_contact_successful(name))
            case 5:
                pb = my_pb.load()
                info = view.input_find_contact()
                your_contact = my_pb.find(pb, info, text.find_contact_error)
                view.print_contact(your_contact, text.find_contact_error)

            case 6:
                pb = my_pb.load()
                info = view.input_find_contact()
                view.print_contact(pb, text.load_error)
                name = view.input_contact(text.new_contact, text.cancel_input)
                change_pb = my_pb.change(info, name, text.find_contact_error)
                view.print_message(text.change_pb)
                
            case 7:
                pb = my_pb.load()
                index = view.input_index(text.index_del_contact, pb, text.load_error)
                name = my_pb.dellcont(index)
                view.print_message(text.del_contact(name))
                
            case 8:
                view.print_message(text.close_pb)
                break