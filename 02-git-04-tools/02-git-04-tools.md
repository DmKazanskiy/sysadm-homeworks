 # Домашнее задание к занятию «2.4. Инструменты Git»

1. Найдите полный хеш и комментарий коммита, хеш которого начинается на `aefea`.
`git log aefea -n 1 --format="Полный хэш: %H;%nКомментарий коммита: %s"`
![[Pasted image 20211121201940.png]]

2. Какому тегу соответствует коммит `85024d3`?
tag `v0.12.23^0`
![[Pasted image 20211121204046.png]]

3. Сколько родителей у коммита `b8d720`? Напишите их хеши.
у заданного хэша два родителя:
```
parent 56cd7859e05c36c06b56d013b55a252d0bb7e158
parent 9ea88f22fc6269854151c571162c5bcf958bee2b

```
![[Pasted image 20211121210946.png]]

4. Перечислите хеши и комментарии всех коммитов которые были сделаны между тегами v0.12.23 и v0.12.24.
```
Hash: 33ff1c03bb960b332be3af2e333462dde88b279e; Comments: v0.12.24
Hash: b14b74c4939dcab573326f4e3ee2a62e23e12f89; Comments: [Website] vmc provider links
Hash: 3f235065b9347a758efadc92295b540ee0a5e26e; Comments: Update CHANGELOG.md
Hash: 6ae64e247b332925b872447e9ce869657281c2bf; Comments: registry: Fix panic when server is unreachable
Hash: 5c619ca1baf2e21a155fcdb4c264cc9e24a2a353; Comments: website: Remove links to the getting started guide's old location
Hash: 06275647e2b53d97d4f0a19a0fec11f6d69820b5; Comments: Update CHANGELOG.md
Hash: d5f9411f5108260320064349b757f55c09bc4b80; Comments: command: Fix bug when using terraform login on Windows
Hash: 4b6d06cc5dcb78af637bbb19c198faff37a066ed; Comments: Update CHANGELOG.md
Hash: dd01a35078f040ca984cdd349f18d0b67e486c35; Comments: Update CHANGELOG.md
Hash: 225466bc3e5f35baa5d07197bbc079345b77525e; Comments: Cleanup after v0.12.23 release
```
![[Pasted image 20211121211704.png]]

5. Найдите коммит в котором была создана функция `func providerSource`, ее определение в коде выглядит так `func providerSource(...)` (вместо троеточего перечислены аргументы).

`git log -S'func providerSource(' --format='%H'` = 8c928e83589d90a031f811fae52a81be7153e82f

![[Pasted image 20211124205355.png]]

6. Найдите все коммиты в которых была изменена функция `globalPluginDirs`.

`git grep --break --heading -n -p 'func globalPluginDirs'`
`git log -L :'func globalPluginDirs':plugins.go --no-patch| grep commit`
commit 78b12205587fe839f10d946ea3fdc06719decb05
commit 52dbf94834cb970b510f2fba853a5b49ad9b1a46
commit 41ab0aef7a0fe030e84018973a64135b11abcd70
commit 66ebff90cdfaa6938f26f908c7ebad8d547fea17
commit 8364383c359a6b738a436d1b7745ccdce178df47

![[Pasted image 20211124210303.png]]

7. Кто автор функции `synchronizedWriters`?

`git log -S synchronizedWriters --format='%h, %an, %ad'`
5ac311e2a, Martin Atkins, Wed May 3 16:25:41 2017 -0700

![[Pasted image 20211124211647.png]]
