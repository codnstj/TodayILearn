#!/usr/bin/env python

import os
from urllib import parse

HEADER="""# 
# Today I Learn

**규칙!**

> 1.  하루의 공부량을 거짓되게 적지 않는다.
> 2.  파일 형식은 mdLearn.md 를 참고하여 md 파일을 작성한다.
> 3.  md 파일 을 작성할떄 필요시 링크를 첨부한다.
> 4.  **열심히 매우 열심히 한다.!**

> 2020 12/22 부터 시작함.


---
"""

def main():
    content = ""
    content += HEADER
    
    directories = [];

    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)
        
        if category == 'images':
            continue
        
        directory = os.path.basename(os.path.dirname(root))
        
        if directory == '.':
            if len(files) == 1:
                content += "### [{}]({})\n".format(category, parse.quote(os.path.join(root, files[0])))
                directories.append(category)
            continue
            
        if directory not in directories:
            content += "### {}\n".format(directory)
            directories.append(directory)

        for file in files:
            content += "- [{}]({})\n".format(category, parse.quote(os.path.join(root, file)))
        content += "\n"

    with open("README.md", "w") as fd:
        fd.write(content)


if __name__ == "__main__":
    main()