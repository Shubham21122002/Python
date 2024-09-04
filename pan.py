import pandas as pd
import numpy as np


print(">>>>>>>>>>>>>>>>>>series<<<<<<<<<<<<<<<<<<");

a=np.array([1,2,3,4,5]);
b=pd.Series(a,index=['a','b','c','d','e']);
print(b);


print("axes :",b.axes);

print("data type  :",b.dtype);

print("is empty  :",b.empty);

print("diamensions  :",b.ndim);

print(" Size: ",b.size);

print(" values: ",b.values);

print(">>>>>>>>>>>>>>>>>>data frame<<<<<<<<<<<<<<<<<<");

c=[["shubham",'20',"male"],["Anikert",'30','male'],["anisha",'20','female'],["nakul",'22','male']];
d=pd.DataFrame(c,index=[1,2,3,4],columns=["Name","age","gender"]);
print(d);

e={'A':[1,2,3,4],'B':[2,3,4,4],'C':[1,2,3,4]};
f=pd.DataFrame(e);
print(f);


print("count:\n",f.count());

print("sum:\n",f.sum());

print("sum:\n",f.sum());

print("mean:\n",f.mean());

print("median:\n",f.median());

print("mode:\n",f.mode());

print("max:\n",f.max());

print("min:\n",f.min());














