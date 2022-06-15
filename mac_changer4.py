from email import parser
import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest = "interface", help="Comando para selecionar la interaz de red")
parser.add_option("-m", "--mac", dest = "new_mac", help="Comando para cambiar direccion MAC")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("[+] La Mac de la intefaz de red " + interface + " ha sido cambiada a " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])