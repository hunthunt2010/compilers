int x = 1 << 2;
int y = 1 << x;

if ( y > 2 )
{
    return 0;
} else
{
    y = y << 1;
}

return y;