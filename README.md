# ParamFirstCheck
ParamFirstCheck identifies in a list of urls those containing the top 25 of the most vulnerable parameters to SQLi, LFI, RCE and Open redirect

## Install:
```bash
$ git clone https://github.com/mathis2001/ParamFirstCheck
```

## Usage:
```bash
$ cat urls.txt | python3 ParamFirstCheck.py

or with an other tool like waybackurls

$ waybackurls exemple.com | python3 ParamFirstCheck.py
```
## Screeenshots

![tempsnip](https://user-images.githubusercontent.com/40497633/183649507-3023f81b-2094-457a-9953-bde3d539d162.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/183648302-b7132d47-4754-47b5-9801-37e914c4e108.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/183648869-f01c4ca6-6f15-493b-ad0c-8d3ed11cccd9.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/183649066-9075ae9d-59d9-468a-b89b-db05f15bd8af.png)
