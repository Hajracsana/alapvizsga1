import random
import math
atmero = int(input('Kérem az óra átmérőjét (mm): '))
lista = ['kék', 'piros', 'zöld']
print(f'Az óra színe: {random.choice(lista)}')
print(f'A védőfólia mérete: {atmero/2 * atmero/2 * math.pi :.2f} mm2')
