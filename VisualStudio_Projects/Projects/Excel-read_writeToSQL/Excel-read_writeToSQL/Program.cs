using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Diagnostics;
using System.Data;
using System.Data.SqlClient;
using System.Data.SqlTypes;
using System.ComponentModel;
using OfficeOpenXml;
using OfficeOpenXml.Drawing;
using ConsoleDump;

namespace Excel_read_writeToSQL
{

    class Program
    {
        public static SqlDbType GetDBType(Type theType)
        {
            SqlParameter p1 = new SqlParameter();
            TypeConverter tc = TypeDescriptor.GetConverter(p1.DbType);

            p1.DbType = (DbType)tc.ConvertFrom(theType.Name);

            return p1.SqlDbType;
        }

        public Dictionary<int, List<string>> read_Excel(string path_excel, string sheet_name)
        {
            ExcelPackage package = new ExcelPackage(new FileInfo(path_excel));
            List<string> sheet_names = new List<string>();
            foreach (var excelWorksheet in package.Workbook.Worksheets)
            {
                string sheet_name2 = Convert.ToString(excelWorksheet.Name);
                sheet_names.Add(sheet_name2);
            }
            int index = sheet_names.IndexOf(sheet_name);
            Dictionary<int, List<string>> data_rows;
            if (index > -1)
            {
                ExcelWorksheet worksheet = package.Workbook.Worksheets.ElementAt(index);
                data_rows = data_list(worksheet);
            }
            else
            {
                Console.WriteLine("\nSheet name doesn't match, using first sheet.\n");
                ExcelWorksheet worksheet = package.Workbook.Worksheets.First();
                data_rows = data_list(worksheet);
            }
            return data_rows;
        }

        public Dictionary<int, List<string>> data_list(ExcelWorksheet worksheet)
        {
            Dictionary<int, List<string>> data_rows = new Dictionary<int, List<string>>();
            int rangeMaxRows = worksheet.Dimension.End.Row;
            int rangeMaxColumns = worksheet.Dimension.End.Column;
            for (int iRow = 0; iRow < rangeMaxRows; iRow++)
            {
                List<string> data_row = new List<string>();
                for (int iCol = 0; iCol < rangeMaxColumns; iCol++)
                {
                    data_row.Add(Convert.ToString((worksheet.Cells[iRow+1, iCol+1]).Value));
                }
                data_rows.Add(iRow, data_row);
            }
            return data_rows;
        }

        public SqlConnection SQL_connection(string data_source, string database, string user_ID, string password)
        {
            string connectionString = "Data source=" + data_source + "; Database=" + database + ";User Id=" + user_ID + ";Password=" + password;
            SqlConnection connection = new SqlConnection(connectionString);
            return connection;
        }

        private System.Data.SqlDbType GetSQLType(string type)
        {
            return (SqlDbType)Enum.Parse(typeof(SqlDbType), type);
        }

        public List<SqlDbType> SQL_readTable_columnTypes(SqlConnection connection, string table_name)
        {
            System.Globalization.CultureInfo ci = System.Globalization.CultureInfo.GetCultureInfo("en-GB");
            try
            {
                SqlDbType[] SQLDbTypes = (SqlDbType[])Enum.GetValues(typeof(SqlDbType));
                string[] SQLDbTypes_ToUpper = Array.ConvertAll((SqlDbType[])Enum.GetValues(typeof(SqlDbType)), type => type.ToString().ToUpper(ci));

                List<SqlDbType> data_column_types = new List<SqlDbType>();
                List<string> data_column_names = new List<string>();
                using (SqlCommand command_read = new SqlCommand("select * from " + table_name, connection))
                {
                    using (SqlDataReader reader = command_read.ExecuteReader())
                    {
                        for (int col = 0; col < reader.FieldCount; col++)
                        {
                            int index = SQLDbTypes_ToUpper.ToList().IndexOf(reader.GetDataTypeName(col).ToUpper(ci));
                            data_column_types.Add(SQLDbTypes[index]);
                            data_column_names.Add(reader.GetName(col));
                        }
                    }
                }
                return data_column_types;
            }
            catch (Exception e)
            {
                Console.WriteLine("Error: Cannot read the table.");
                Console.WriteLine("[Error message:] " + e.Message);
                return new List<SqlDbType>();
            }
        }

        public void SQL_readTable(SqlConnection connection, string table_name)
        {
            try
            {
                List<object> data_column_types = new List<object>();
                List<object> data_column_names = new List<object>();
                Dictionary<int, object> data_rows = new Dictionary<int, object>();
                string commandText = "select * from " + table_name;
                SqlCommand command = new SqlCommand(commandText, connection);
                SqlDataReader reader = command.ExecuteReader();
                while (reader.Read())
                {
                    Console.WriteLine(reader.GetName(0));
                    //Console.WriteLine(reader.FieldCount);
                    //Console.Write(reader["col1"].GetType());
                    //Console.Write(" ");
                    //Console.WriteLine(reader["col2 col2"].GetType());
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Error: Cannot read the table.");
                Console.WriteLine("[Error message:] " + e.Message);
            }
        }

        public void SQL_createTable(SqlConnection connection, string table_name, Dictionary<int, List<string>> data_list)
        {
            try
            {
                string commandText = "CREATE TABLE " + table_name;
                foreach (string data_name in data_list[0])
                {

                }
                //using (SqlCommand command = new SqlCommand(
                //    "CREATE TABLE Dogs1 (Weight INT, Name TEXT, Breed TEXT)", connection))
                //{
                //    command.ExecuteNonQuery();
                //}
            }
            catch (Exception e)
            {
                Console.WriteLine("Error: Cannot create the table.");
                Console.WriteLine("[Error message:] " + e.Message);
            }
        }

        public void SQL_insertINTO(SqlConnection connection, string table_name, Dictionary<int, List<string>> data_list)
        {
            System.Globalization.CultureInfo ci = System.Globalization.CultureInfo.GetCultureInfo("en-GB");
            try
            {
                SqlDbType[] SQLDbTypes = (SqlDbType[])Enum.GetValues(typeof(SqlDbType));
                string[] SQLDbTypes_ToUpper = Array.ConvertAll((SqlDbType[])Enum.GetValues(typeof(SqlDbType)), type => type.ToString().ToUpper(ci));

                List<SqlDbType> data_column_types = new List<SqlDbType>();
                List<string> data_column_names = new List<string>();
                using (SqlCommand command_read = new SqlCommand("select * from " + table_name, connection))
                {
                    using (SqlDataReader reader = command_read.ExecuteReader())
                    {
                        for (int col = 0; col < reader.FieldCount; col++)
                        {
                            int index = SQLDbTypes_ToUpper.ToList().IndexOf(reader.GetDataTypeName(col).ToUpper(ci));
                            data_column_types.Add(SQLDbTypes[index]);
                            data_column_names.Add(reader.GetName(col));
                        }
                    }
                }
                
                string insertNames = "[" + data_list[0][0] + "]";
                for (int col = 1; col < data_list[0].Count; col++) { insertNames += ", [" + data_list[0][col] + "]"; }

                string insertValues = "@param0";
                for (int col = 1; col < data_list[0].Count; col++) { insertValues += ", @param" + Convert.ToString(col); }

                string commandText_write = "INSERT INTO " + table_name + "(" + insertNames + ")" + "VALUES(" + insertValues + ")";

                using (SqlCommand command_write = new SqlCommand(commandText_write, connection))
                {
                    for (int row = 1; row < data_list.Count(); row++)
                    {
                        for (int col = 0; col < data_list[0].Count; col++)
                        {
                            SqlParameter param = command_write.CreateParameter();
                            param.ParameterName = "@param" + Convert.ToString(col);
                            param.Value = data_list[row][col];
                            //Console.WriteLine(data_list[row][col].GetType());
                            param.SqlDbType = data_column_types[col];
                            //param.Direction = ParameterDirection.Input;
                            command_write.Parameters.Add(param);
                        }
                        command_write.ExecuteNonQuery();
                        command_write.Parameters.Clear();
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("\nError: Cannot insert data.");
                Console.WriteLine("[Error message:] " + e.Message);
            }
        }
        

        static void Main(string[] args)
        {
            Program program = new Program();

            //Console.WriteLine("\nPath of excel file:");
            //string path_excel = Console.ReadLine();

            //Console.WriteLine("\nFocus on sheet (press enter if you want to use first worksheet):");
            //string sheet_name = Console.ReadLine();

            //Dictionary<int, List<string>> data_list = program.read_Excel(path_excel, sheet_name);
            ////Console.WriteLine(data_list[0].Dump());

            //Console.WriteLine("\nSQL server info;");
            //Console.Write("data source=");
            //string data_source = Console.ReadLine();
            //Console.Write("database=");
            //string database = Console.ReadLine();
            //Console.Write("user id=");
            //string user_ID = Console.ReadLine();
            //Console.Write("password=");
            //string password = Console.ReadLine();

           //data source=morpheus;initial catalog=Stoneluxxe;persist security info=False;user id=Stoneluxxe;password=Stoneluxxe857452;multipleactiveresultsets=False;App=EntityFramework&quot;" providerName = "System.Data.EntityClient" />
            SqlConnection connection = program.SQL_connection("morpheus", "Stoneluxxe", "Stoneluxxe", "Stoneluxxe857452");
            //SqlConnection conn = program.connection(data_source, database, user_ID, password);
            bool connected;
            try
            {
                connection.Open();
                connected = true;
            }
            catch (Exception e)
            {
                Console.WriteLine("\nError: Cannot connect to server database.");
                Console.WriteLine("[Error message:] " + e.Message);
                connected = false;
            }
            if (connected==true)
            {
                Console.WriteLine("\nConnected to server database.");

                //Console.WriteLine("\nWhat do you want to do now with data you get from excel file?");
                //Console.WriteLine("  1) Create or update a database with input data.");
                //Console.WriteLine("  2) Insert input data into a database.");
                //Console.WriteLine("##Choose one of the actions at top.[actions: 1 or 2]##\n");
                //string action = Console.ReadLine();

                //Console.WriteLine("\nDo operations on which table?\n(write table name at [owner].[table] format such as [dbo].[Contact])");
                //string table_name = Console.ReadLine();
                string table_name = "[dbo].[test]";

                Dictionary<int, List<string>> data_list = new Dictionary<int, List<string>>();
                List<string> data_row1 = new List<string>();
                data_row1.Add("col1");
                data_row1.Add("col2 col2");
                data_list.Add(0, data_row1);
                List<string> data_row2 = new List<string>();
                data_row2.Add("test20");
                data_row2.Add("test20");
                data_list.Add(1, data_row2);
                List<string> data_row3 = new List<string>();
                data_row3.Add("test21");
                data_row3.Add("test21");
                data_list.Add(2, data_row3);

                //program.SQL_insertINTO(connection, table_name, data_list);
                List<SqlDbType> a = program.SQL_readTable_columnTypes(connection, table_name);
                //Console.WriteLine(a.Dump());
                SqlDbType[] SQLTypeNames = (SqlDbType[])Enum.GetValues(typeof(SqlDbType));
                DbType[] TypeNames = (DbType[])Enum.GetValues(typeof(DbType));

                Console.WriteLine(TypeNames.Dump());
                try
                {
                    int strVar = 111;
                    
                    //Console.WriteLine(GetDBType(strVar.GetType()));
                    //Console.WriteLine(program.GetSQLType("NVarChar"));
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
                connection.Close();

            }

            Console.WriteLine("\nPress any key to exit...");
            Console.ReadKey();
        }
        
    }
}
