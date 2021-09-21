import os
from rich.console import Console
from rich.text import Text
console = Console()


def rich_func(res):
	console.print(Text(res, style="bold blue"))


def Status_of_firewall():
	ram = os.popen("sudo ufw status").read()
	rich_func(ram)


def Delete_rules():
	res = os.popen("sudo ufw status numbered").read()
	rich_func(res)
	index = input("Please enter the index number of the rule to be deleted :  ")
	res1 = os.popen(f"sudo ufw delete {index}").read()
	rich_func(res1)

	
def Reload_rules():
	res = os.popen("sudo ufw reload").read()
	rich_func(res)


def rule_menu():

	console.print("1.Disable the firewall", style="bright_magenta")
	console.print("2.Block the Host IP", style="bright_magenta")
	console.print("3.Allow the Host IP", style="bright_magenta")
	console.print("4.Allow Port", style="bright_magenta")
	console.print("5.Block Port", style="bright_magenta")
	console.print("6.Allow a subnet", style="bright_magenta")
	console.print("7.Get Firewall app list", style="bright_magenta")
	console.print("8.Show Rules Added", style="bright_magenta")
	console.print("9.Exit", style="bright_magenta")


def activate_ufw():
	res = os.popen("sudo ufw enable").read()
	
	result = print(res)
	return result


def Exit():
	exit()


def set_rules():
	rule_menu()
	ch = input("Please enter your choice")
	if ch == '1':
		res = os.popen("sudo ufw disable").read()
		rich_func(res)

	elif ch == '2':
		ip = input("Enter the IP to block : ")
		print(ip)
		res = os.popen(f"sudo ufw deny from {ip}").read()
		rich_func(res)

	elif ch == '3':
		ip = input("Enter the IP to allow")
		res = os.popen(f"sudo ufw allow from {ip}").read()
		rich_func(res)

	elif ch == '4':
		port = input("Enter the Port Number to allow: ")
		res = os.popen(f"sudo ufw allow {port}").read()
		rich_func(res)

	elif ch == '5':
		port = input("Enter the Port Number to block")
		res = os.popen(f"sudo ufw deny {port}").read()
		rich_func(res)

	elif ch == '6':
		subnet = input("Enter the subnet to allow")
		res = os.popen(f"sudo ufw allow from {subnet}").read()
		rich_func(res)

	elif ch == '7':
		res = os.popen("sudo ufw app list").read()
		rich_func(res)
			
	elif ch == '8':
		res = os.popen("sudo ufw status numbered").read()
		rich_func(res)
			
	elif ch == '9':
		exit()


def main_menu():
	console.print("1.Status of firewall", style="bright_magenta")
	console.print("2.Set Rules", style="bright_magenta")
	console.print("3.Delete Rules", style="bright_magenta")
	console.print("4.Reload Rules", style="bright_magenta")
	console.print("5.Exit", style="bright_magenta")


operations = {
	"1": Status_of_firewall,
	"2": set_rules,
	"3": Delete_rules,
	"4": Reload_rules,
	"5": Exit
}

while True:
	main_menu()
	choice = input("Please enter the Choice: ")
	activate_ufw()
	operations[choice]()
