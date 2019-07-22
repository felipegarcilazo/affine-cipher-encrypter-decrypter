import tkinter as tk
import math
import tools

class Application(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.crypt = tk.StringVar()
        self.crypt.set("enc")
        self.lbl = tk.Label(self, text='Alphabet:').grid(row=0, column=0, sticky=tk.W)
        self.ent1 = tk.Entry(self, width=40)
        self.ent1.grid(row=0, column=1, columnspan=3)
        self.ent1.insert(0, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,. ;:?")
        self.lbl1 = tk.Label(self, text="Multiplication Key:").grid(row=1, column=0, sticky=tk.W)
        self.ent2 = tk.Entry(self, width=5)
        self.ent2.grid(row=1, column=1)
        self.ent2.insert(0, "1")
        self.lbl2 = tk.Label(self, text="Addition Key:").grid(row=2, column=0, sticky=tk.W)
        self.ent3 = tk.Entry(self, width=5)
        self.ent3.grid(row=2, column=1)
        self.ent3.insert(0, "1")
        self.lbl3 = tk.Label(self, text="Choose to encrypt or decrypt:").grid(row=3, column=0, sticky=tk.W)
        self.rad1 = tk.Radiobutton(self, text = "Encrypt", variable = self.crypt, value = "enc").grid(row=3, column=1)
        self.rad2 = tk.Radiobutton(self, text = "Decrypt", variable = self.crypt, value = "dec").grid(row=3, column=2)
        self.lbl4 = tk.Label(self, text="Text to be Encrypted or Decrypted:").grid(row=4, column=0, columnspan=2, sticky=tk.E)
        self.txt = tk.Text(self, width = 60, height=15, wrap=tk.WORD)
        self.txt.grid(row=5, column=0, columnspan=5)
        self.bttn = tk.Button(self, text="Encrypt/Decrypt!!", command=self.solv).grid(row=6, column=1) 

    def solv(self):
        mode_c, alphabet, mult_key, add_key, txt_inp = self.crypt.get(), self.ent1.get(), self.ent2.get(), self.ent3.get(), self.txt.get(0.0, END)
        if math.gcd(int(len(alphabet)), int(mult_key))!=1:
            result = "ERROR: Multiplication key does not have a valid inverse. Or a non-digit number was inputed."
        else:
            if mode_c == "enc":
                result = tools.encrypt(alphabet, mult_key, add_key, txt_inp)
            else:
                result = tools.decrypt(alphabet, mult_key, add_key, txt_inp)
        self.txt.delete(0.0, END)
        self.txt.insert(0.0, result)
                
# main
root = tk.Tk()
root.title("Decrypter and Encrypter of Affine Cypher")
root.geometry("600x400")
root.resizable(width = tk.FALSE, height = tk.FALSE)
app = Application(root)
root.mainloop()

if __name__ == '__main__':
    try:
        Application()
    except Exception as e:
        print('Error:', str(e))
