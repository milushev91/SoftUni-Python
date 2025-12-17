flour_kg_price = float(input())
flour_kgs_count = float(input())

suggar_kgs_count = float(input())
egg_shells_count = int(input())
yeast_packages_count = int(input())

suggar_kg_price = flour_kg_price - flour_kg_price * 0.25 
egg_shell_price = flour_kg_price * 1.10
yeast_package_price = suggar_kg_price - suggar_kg_price * 0.80

flour_price = flour_kgs_count * flour_kg_price
suggar_price = suggar_kgs_count * suggar_kg_price
egg_shells_price = egg_shells_count * egg_shell_price
yeast_packages_price = yeast_packages_count * yeast_package_price

total_price = flour_price + suggar_price + egg_shells_price +\
    yeast_packages_price

print(f"{total_price:.2f}")
