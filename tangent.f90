program tann
implicit none
real::a,b,c,d,e,f,e1
integer::i,j,k,l

character(len=30)::junk
open(1,file='titanium.pdos_tot' ,status='old',action='read')
read(1,*)junk
read(1,*)a,e1
read(1,*)a,e
f=(e-e1)/0.01
do i=1,5974
read(1,*)a,b
c=(b-e)/0.01


d=sign(c,f)

if (c .ne. d .and. d .gt. 0.d0) write(*,*)a,b

f=c
write(88,*)a,c 
e=b
end do
end program tann

