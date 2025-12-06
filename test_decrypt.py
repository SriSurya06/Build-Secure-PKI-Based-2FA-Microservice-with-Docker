from crypto_utils import load_private_key, decrypt_seed

private_key = load_private_key("student_private.pem")

encrypted_seed = """HU+6doA5fJE12FDTlJ0hUyoyydg28o5jR91bkq6Uxnud+lvjZOjM3oY+SIo7ZJEJUASDUiCi84h78Hjbx0E/aeW7hKOJKYzPNvy3MgtSzt9obwASL8NNlNT7qSWtZNbwRH0l0k59N9yxm6+fdwnonU9RxCkBJDopjKQSD6Q0Uf0l/Onses6v7GadAdEHd3J74scZxhbIjum/MpNlCmlh6WimyrYh1isLDVd3olEgqGxiqI4oq6448CQmTnRQzQjk07u/u7iiRze8+fepWBLzau0yPT1KH9lhbREcbqmD//mnKQnNS6jM5oFdfLFexCZM8Z6uy4lAuqIQkHim+LNvnDWiRriPIrqEG0t4wbSYIO7PpRw1eJKCv+6SyUX5P7lDvLaDJNwA2vqzmHxre9l4seU+2PSypQN8RUikTCZK4qmWLhRxECWQ+a0uKywXIIV9jFX0UgSi3tE5dDR2lVFCOSOAOxL5zNW4+rvqhljf0anths5P1rxT7vCAqYTRlQ3hQTH3dPibc1P4z/hdMzM01QTd4OUUXoXSlX7bw6yFhQGSln+P1FWVShdK/B9qosZtJFDQ8mueEEVzBedkb4mOnony2Gb++AJGseLrGy+BZ+0fp3wkgqC0Zqgzncz6/YUDrlt9HIxgRCAI/fcDd/yvsaOtrS35w61LxdpfSJg80rQ="""


encrypted_seed = encrypted_seed.strip()

try:
    seed = decrypt_seed(encrypted_seed, private_key)
    print("Decrypted seed:", seed)
except Exception as e:
    print("Error:", e)
