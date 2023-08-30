import random

def generate_code():
  """Generates a random four digit code."""
  return ''.join([str(random.randint(0, 9)) for i in range(4)])

def main():
  """Generates and prints unlimited random four digit codes."""
  while True:
    code = generate_code()
    print(code)

if __name__ == '__main__':
  main()