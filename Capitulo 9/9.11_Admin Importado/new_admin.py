from Admin import Admin
from Privilegios import Privilegios as prv

new_admin = Admin('joaquin', 'de souza', 'joade', 'argentina')
new_privilegios = prv(None)

new_admin.describir_usuario()
new_privilegios.show_privileges()