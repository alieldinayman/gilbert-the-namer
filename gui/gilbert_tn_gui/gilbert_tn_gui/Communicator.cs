using System;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
using System.Runtime.Remoting;

namespace gilbert_tn_gui
{
    /// <summary>
    /// Used for communicating with the python wrapper
    /// </summary>
    class Communicator
    {
        ScriptEngine gilPY;
        ScriptScope gilScope;
        Object gilClass;

        public Communicator()
        {
            gilPY = Python.CreateEngine();
            gilScope = gilPY.CreateScope();

            try
            {
                gilPY.ExecuteFile("C:\\Users\\series3\\Documents\\GitHub\\gilbert-the-namer\\wrapper\\pynet_wrapper.py", gilScope);
                gilClass = gilPY.Operations.Invoke(gilScope.GetVariable("GilbertWrapper"));
            }
            catch (Exception e)
            {
                Console.WriteLine("Couldn't initiate python wrapper. Error : " + e.Message);
            }
        }

        public dynamic ExecuteFunctionWithReturn(string functionName, params dynamic[] args)
        {
            try
            {
                return gilPY.Operations.InvokeMember(gilClass, functionName, args);
            }
            catch(Exception e)
            {
                Console.WriteLine("Error calling method: " + e);
                return "Error calling method";
            }
        }

        public void ExecuteFuntion(string functionName, params dynamic[] args)
        {
            try
            {
                gilPY.Operations.InvokeMember(gilClass, functionName, args);
            }
            catch (Exception e)
            {
                Console.WriteLine("Error calling method: " + e);
            }
        }
    }
}
