{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "18b3650f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world\n"
     ]
    }
   ],
   "source": [
    "print(\"hello world\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "70610660",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world 3\n"
     ]
    }
   ],
   "source": [
    "print(\"hello world\",3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bae23bdf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "value of c : 48\n"
     ]
    }
   ],
   "source": [
    "a=19\n",
    "b=29\n",
    "c=a+b\n",
    "print(\"value of c :\",c )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "16de933c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "print(type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b838b640",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "19.0\n"
     ]
    }
   ],
   "source": [
    "a=19\n",
    "print(float(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b6e9bb33",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "52\n"
     ]
    }
   ],
   "source": [
    "a=29.33\n",
    "b=23.33\n",
    "c=a+b\n",
    "print(int(a)+int(b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "25bcc2c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "52 52.66\n"
     ]
    }
   ],
   "source": [
    "a=29.33\n",
    "b=23.33\n",
    "c=a+b\n",
    "print(int(a)+int(b),c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e0e4d8f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sum of a and b is: 30\n",
      "sub of a and b is: -10\n",
      "mul of a and b is: 200\n",
      "div of a and b is: 0.5\n",
      "mod of a and b is: 0\n"
     ]
    }
   ],
   "source": [
    "a=10\n",
    "b=20\n",
    "print(\"sum of a and b is:\",a+b)\n",
    "print(\"sub of a and b is:\",a-b)\n",
    "print(\"mul of a and b is:\",a*b)\n",
    "print(\"div of a and b is:\",a/b)\n",
    "print(\"mod of a and b is:\",a//b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "549cbd3b",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'intput' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[18], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m a\u001b[38;5;241m=\u001b[39m\u001b[43mintput\u001b[49m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124menter a number:\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      2\u001b[0m b\u001b[38;5;241m=\u001b[39m\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124menter a number:\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msum of a and b is:\u001b[39m\u001b[38;5;124m\"\u001b[39m,a\u001b[38;5;241m+\u001b[39mb)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'intput' is not defined"
     ]
    }
   ],
   "source": [
    "a=intput(\"enter a number:\")\n",
    "b=input(\"enter a number:\")\n",
    "print(\"sum of a and b is:\",a+b)\n",
    "print(\"sub of a and b is:\",a-b)\n",
    "print(\"mul of a and b is:\",a*b)\n",
    "print(\"div of a and b is:\",a/b)\n",
    "print(\"mod of a and b is:\",a//b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "e205c57a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number:88\n",
      "enter a number:44\n",
      "sum of a and b is: 8844\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for -: 'str' and 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[19], line 4\u001b[0m\n\u001b[0;32m      2\u001b[0m b\u001b[38;5;241m=\u001b[39m\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124menter a number:\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msum of a and b is:\u001b[39m\u001b[38;5;124m\"\u001b[39m,a\u001b[38;5;241m+\u001b[39mb)\n\u001b[1;32m----> 4\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msub of a and b is:\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[43ma\u001b[49m\u001b[38;5;241;43m-\u001b[39;49m\u001b[43mb\u001b[49m)\n\u001b[0;32m      5\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmul of a and b is:\u001b[39m\u001b[38;5;124m\"\u001b[39m,a\u001b[38;5;241m*\u001b[39mb)\n\u001b[0;32m      6\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdiv of a and b is:\u001b[39m\u001b[38;5;124m\"\u001b[39m,a\u001b[38;5;241m/\u001b[39mb)\n",
      "\u001b[1;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'str' and 'str'"
     ]
    }
   ],
   "source": [
    "a=input(\"enter a number:\")\n",
    "b=input(\"enter a number:\")\n",
    "print(\"sum of a and b is:\",a+b)\n",
    "print(\"sub of a and b is:\",a-b)\n",
    "print(\"mul of a and b is:\",a*b)\n",
    "print(\"div of a and b is:\",a/b)\n",
    "print(\"mod of a and b is:\",a//b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "6c2857b5",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax. Perhaps you forgot a comma? (1570266542.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[20], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    a=input(enter a number:)\u001b[0m\n\u001b[1;37m            ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax. Perhaps you forgot a comma?\n"
     ]
    }
   ],
   "source": [
    "a=input(enter a number:)\n",
    "b=input(enter a number:)\n",
    "print(\"sum of a and b is:\",a+b)\n",
    "print(\"sub of a and b is:\",a-b)\n",
    "print(\"mul of a and b is:\",a*b)\n",
    "print(\"div of a and b is:\",a/b)\n",
    "print(\"mod of a and b is:\",a//b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "e10f1816",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number:55\n",
      "enter a number:99\n",
      "sum of a and b is: 154\n",
      "sub of a and b is: -44\n",
      "mul of a and b is: 5445\n",
      "div of a and b is: 0.5555555555555556\n",
      "mod of a and b is: 0\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter a number:\"))\n",
    "b=int(input(\"enter a number:\"))\n",
    "print(\"sum of a and b is:\",a+b)\n",
    "print(\"sub of a and b is:\",a-b)\n",
    "print(\"mul of a and b is:\",a*b)\n",
    "print(\"div of a and b is:\",a/b)\n",
    "print(\"mod of a and b is:\",a//b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "ecad8b01",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number:64\n"
     ]
    }
   ],
   "source": [
    "a=float(input(\"enter a number:\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "f12885f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "64.0\n"
     ]
    }
   ],
   "source": [
    "print(float(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "340da410",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2456883923472\n"
     ]
    }
   ],
   "source": [
    "print(id(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "f31ecc42",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2456780407312 2456780407920\n"
     ]
    }
   ],
   "source": [
    "a=10\n",
    "b=29\n",
    "print(id(a),id(b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "367fbf24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2456780407312 2456780407312\n"
     ]
    }
   ],
   "source": [
    "a=10\n",
    "b=10\n",
    "print(id(a),id(b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "448549b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sum of values a nd b: 51\n",
      "sum of valus c and a: 93\n"
     ]
    }
   ],
   "source": [
    "a=28\n",
    "b=23\n",
    "c=65\n",
    "print(\"sum of values a nd b:\",a+b)\n",
    "print(\"sum of valus c and a:\",c+a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec2e0507",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
