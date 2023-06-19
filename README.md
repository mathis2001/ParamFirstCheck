# ParamFirstCheck
ParamFirstCheck identifies in a list of urls those containing the top 25 of the most vulnerable parameters to SQLi, LFI, RCE and Open redirect

## Install:
```bash
$ git clone https://github.com/mathis2001/ParamFirstCheck
```

## Usage:
```bash
$ cat urls.txt | python3 ParamFirstCheck.py [--sql] [--rce] [--lfi] [--open-redirect]

or with an other tool like waybackurls

$ waybackurls exemple.com | python3 ParamFirstCheck.py [--sql] [--rce] [--lfi] [--open-redirect]
```
## Screenshots

![tempsnip](https://user-images.githubusercontent.com/40497633/183855360-874da841-14a3-4679-8ec3-34d5568b2155.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/183855664-7bc3719e-80b1-417a-9752-cf9d76a241dd.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/183856001-6ca9d21b-1769-4bd3-a75e-550fb1c97880.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/183856275-1d99ae83-b1ef-4839-90f0-4c033caca1e0.png)
