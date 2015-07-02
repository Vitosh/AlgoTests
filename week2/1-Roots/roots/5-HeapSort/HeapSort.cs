using System;
using System.Collections.Generic;

public class heap
{
	public List<int> myList = new List<int>();
	public int myLen;

	public heap(List<int> myList, int myLen)
	{
		this.myLen = myLen;
		this.myList = myList;
	}
	
	public void hsort()
	{
		int t;

		for (int i = myLen/2; i >= 0; i--)
		{
			adjust(i, myLen-1);
		}

		for (int i = myLen-2; i >= 0; i--)
		{
			t = myList[i + 1];
			myList[i + 1] = myList[0];
			myList[0] = t;
			adjust(0, i);
		}
	}

	private void adjust(int i, int n)
	{
		int t;
		int j;

		try
		{
			t = myList[i];
			j = 2 * i;
			while (j <= n)
			{
				if (j < n && myList[j] < myList[j + 1])
				{
					j++;
				}
				if (t >=myList[j])
				{
					break;
				}
				myList[j / 2] = myList[j];
				j *= 2;
			}
			myList[j / 2] = t;
		}

		catch (Exception e)
		{
			Console.WriteLine(e);
		}
	}

	public string printList()
	{
		string myValue = "";
		for (int i = 0; i < myLen; i++)
		{
			myValue += myList[i] + " ";
		}
		return myValue;
	}

	public static void Main()
	{
		List<int> myList = new List<int>(new int[] {2,5,1,1990,0,6,9,3,7,7,4,8,500,678});
		int myLen = myList.Count;
		heap myHeap = new heap(myList, myLen);

		Console.WriteLine("Original: {0}",myHeap.printList());
		myHeap.hsort();
		Console.WriteLine("Sorted: {0}",myHeap.printList());
	}
}