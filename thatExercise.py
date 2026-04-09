class checker:
    def __init__(self, fileName):
       self.fileName = fileName


    def openFiles(self):
        with open (self.fileName) as f:
            for line in f:
                if line.startswith("From: "):
                    print(line.strip())
        



filechecker = checker("mbox-short.txt")
filechecker.openFiles()