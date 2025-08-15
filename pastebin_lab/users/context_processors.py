def get_menu(request):
    return {'menu': [
                        {'title': 'Главная', 'url_name': 'main'},
                        {'title': 'Контакты', 'url_name': 'contacts'},
                    ]
            }
