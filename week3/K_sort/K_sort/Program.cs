using System;
using System.Collections.Generic;

class MainClass
{
	public static void Main ()
	{
		List myList1 = new List(new int[] {2,5,0,6,9,3,7,7,4,8,500,678});
		List myList2 = new List(new int[] {2,5,678});
		List myList3 = new List(new int[] {2,5,1,1990,0,6,9,3,7,7,4,8,1,1990,0,6,9,3,7,7,4,8,500,678});
		myList1.sort ();
		myList2.sort ();
		myList3.sort ();
	}
}
