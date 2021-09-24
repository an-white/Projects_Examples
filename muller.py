import  math
def f(x):
    #return x**3-13*x-12
    return (40*math.tan(x))+(1.8-1)-((9.81*(40**2))/(2*(20*(math.cos(x)))**2))
xr=45
h=.1

x2=math.radians(xr)
x1=math.radians(xr+h*xr)
x0=math.radians(xr-h*xr)
iter=1
max=12

# muller method for aproximation of roots for quadratics functions
while True:
    iter+=1
    h0 = x1 - x0
    h1 = x2 - x1
    d0 = (f(x1) - f(x0)) / h0
    d1 = (f(x2) - f(x1)) / h1
    a = (d1 - d0) /(h1 + h0)
    b = a*h1 + d1
    c = f(x2)

    rad = math.sqrt(b**2 - 4*a*c)

    if abs(b+rad) > abs(b - rad):
        den = b + rad
    else:
        den = b - rad

    dxr = -2*c /den

    xr = x2 + dxr
    eps=abs((xr-x2)/xr)*100
    print(str(iter-1)+" "+str(math.degrees(xr))+" "+str(eps)+"\n")

    if eps<.1 or iter>=max:
    #if abs(dxr)<eps*xr or iter>=max:
        break
    x0=x1
    x1=x2
    x2=xr