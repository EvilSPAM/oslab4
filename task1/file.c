int sum(int *arr, int len)
{
  int i, res=0;
  for(i = 0; i < len; i++) 
  {
    res += arr[i];
  }
  assert(res == len*(len+1)/2);
  return res;
}

void start(unsigned int n)
{
  __CPROVER_assume(n <= 10);
  int arr[n];
  int i;
  for(i = 0; i < n; i++)
  {
    arr[i] = i+1;
  }
  int s = sum(arr, n);
  assert(s == n*(n+1)/2);
  printf("Sum of %d: %d", n, s);
}