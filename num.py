import numpy as np

a=np.array([1,2,3,4]);
print(a);

print("..........................");

b=np.array([[1,2,3],[3,4,5]])
print("multi:",b);

print("..........................");

c=np.array([1,2,3],ndmin=2)
print("ndmin:",c)

print("..........................");

d=np.dtype(np.int32);
print(d);

print("..........................");

e=np.array([[1,2,3,4],[5,6,7,8]]);
print(e.shape);

print("..........................");

f=np.array([[1,2,3,4],[5,6,7,8]]);
f.shape=(4,2);
print(f);

print("..........................");

print("dimension",f.ndim);

print("..........................");

i=np.arange(6)
print("arange: ",i);

print("..........................");

j=np.array([1,2,3,4]);
print("size of array element:",j.itemsize);

print("..........................");

k=np.                                                                                                                                                                                                                                                                                                                                                                                                                                        zeros(5);
l=np.zeros([2,2],int)
print("zeros: ",k);
print("zeros: ",l);

print("..........................");

m=np.ones(5);
n=np.ones([2,2],int)
print("ones: ",m);
print("ones: ",n);

print("..........................");

o=[1,2,3,4];
p=np.asarray(o);
print("asarray: ",p);

print("..........................");

q=b'hello world';
r=np.frombuffer(q,dtype='S1');
print("frombuffer",r);

print("..........................");

arr = np.full((2, 3), 7)
print("full : ", arr)

print("..........................");

s=np.eye(3)
print("eye : ",s)

print("..........................");

t=np.identity(3)
print("identity: ",t)

print("..........................");

v=np.array([1,2,3])
w=np.array([1,2,3])
u=np.concatenate((v,w));
print("concatenate: ",u);

print("..........................");



