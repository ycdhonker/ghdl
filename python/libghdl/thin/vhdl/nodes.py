from libghdl import libghdl

Null_Iir = 0

Null_Iir_List = 0
Iir_List_All = 1

Null_Iir_Flist = 0
Iir_Flist_Others = 1
Iir_Flist_All = 2



class Iir_Kind:
    Unused = 0
    Error = 1
    Design_File = 2
    Design_Unit = 3
    Library_Clause = 4
    Use_Clause = 5
    Context_Reference = 6
    Integer_Literal = 7
    Floating_Point_Literal = 8
    Null_Literal = 9
    String_Literal8 = 10
    Physical_Int_Literal = 11
    Physical_Fp_Literal = 12
    Simple_Aggregate = 13
    Overflow_Literal = 14
    Unaffected_Waveform = 15
    Waveform_Element = 16
    Conditional_Waveform = 17
    Conditional_Expression = 18
    Association_Element_By_Expression = 19
    Association_Element_By_Individual = 20
    Association_Element_Open = 21
    Association_Element_Package = 22
    Association_Element_Type = 23
    Association_Element_Subprogram = 24
    Choice_By_Range = 25
    Choice_By_Expression = 26
    Choice_By_Others = 27
    Choice_By_None = 28
    Choice_By_Name = 29
    Entity_Aspect_Entity = 30
    Entity_Aspect_Configuration = 31
    Entity_Aspect_Open = 32
    Psl_Hierarchical_Name = 33
    Block_Configuration = 34
    Block_Header = 35
    Component_Configuration = 36
    Binding_Indication = 37
    Entity_Class = 38
    Attribute_Value = 39
    Signature = 40
    Aggregate_Info = 41
    Procedure_Call = 42
    Record_Element_Constraint = 43
    Array_Element_Resolution = 44
    Record_Resolution = 45
    Record_Element_Resolution = 46
    Attribute_Specification = 47
    Disconnection_Specification = 48
    Configuration_Specification = 49
    Access_Type_Definition = 50
    Incomplete_Type_Definition = 51
    Interface_Type_Definition = 52
    File_Type_Definition = 53
    Protected_Type_Declaration = 54
    Record_Type_Definition = 55
    Array_Type_Definition = 56
    Array_Subtype_Definition = 57
    Record_Subtype_Definition = 58
    Access_Subtype_Definition = 59
    Physical_Subtype_Definition = 60
    Floating_Subtype_Definition = 61
    Integer_Subtype_Definition = 62
    Enumeration_Subtype_Definition = 63
    Enumeration_Type_Definition = 64
    Integer_Type_Definition = 65
    Floating_Type_Definition = 66
    Physical_Type_Definition = 67
    Range_Expression = 68
    Protected_Type_Body = 69
    Wildcard_Type_Definition = 70
    Subtype_Definition = 71
    Scalar_Nature_Definition = 72
    Overload_List = 73
    Entity_Declaration = 74
    Configuration_Declaration = 75
    Context_Declaration = 76
    Package_Declaration = 77
    Package_Instantiation_Declaration = 78
    Vmode_Declaration = 79
    Vprop_Declaration = 80
    Vunit_Declaration = 81
    Package_Body = 82
    Architecture_Body = 83
    Type_Declaration = 84
    Anonymous_Type_Declaration = 85
    Subtype_Declaration = 86
    Nature_Declaration = 87
    Subnature_Declaration = 88
    Package_Header = 89
    Unit_Declaration = 90
    Library_Declaration = 91
    Component_Declaration = 92
    Attribute_Declaration = 93
    Group_Template_Declaration = 94
    Group_Declaration = 95
    Element_Declaration = 96
    Non_Object_Alias_Declaration = 97
    Psl_Declaration = 98
    Psl_Endpoint_Declaration = 99
    Terminal_Declaration = 100
    Free_Quantity_Declaration = 101
    Across_Quantity_Declaration = 102
    Through_Quantity_Declaration = 103
    Enumeration_Literal = 104
    Function_Declaration = 105
    Procedure_Declaration = 106
    Function_Body = 107
    Procedure_Body = 108
    Object_Alias_Declaration = 109
    File_Declaration = 110
    Guard_Signal_Declaration = 111
    Signal_Declaration = 112
    Variable_Declaration = 113
    Constant_Declaration = 114
    Iterator_Declaration = 115
    Interface_Constant_Declaration = 116
    Interface_Variable_Declaration = 117
    Interface_Signal_Declaration = 118
    Interface_File_Declaration = 119
    Interface_Type_Declaration = 120
    Interface_Package_Declaration = 121
    Interface_Function_Declaration = 122
    Interface_Procedure_Declaration = 123
    Anonymous_Signal_Declaration = 124
    Signal_Attribute_Declaration = 125
    Identity_Operator = 126
    Negation_Operator = 127
    Absolute_Operator = 128
    Not_Operator = 129
    Implicit_Condition_Operator = 130
    Condition_Operator = 131
    Reduction_And_Operator = 132
    Reduction_Or_Operator = 133
    Reduction_Nand_Operator = 134
    Reduction_Nor_Operator = 135
    Reduction_Xor_Operator = 136
    Reduction_Xnor_Operator = 137
    And_Operator = 138
    Or_Operator = 139
    Nand_Operator = 140
    Nor_Operator = 141
    Xor_Operator = 142
    Xnor_Operator = 143
    Equality_Operator = 144
    Inequality_Operator = 145
    Less_Than_Operator = 146
    Less_Than_Or_Equal_Operator = 147
    Greater_Than_Operator = 148
    Greater_Than_Or_Equal_Operator = 149
    Match_Equality_Operator = 150
    Match_Inequality_Operator = 151
    Match_Less_Than_Operator = 152
    Match_Less_Than_Or_Equal_Operator = 153
    Match_Greater_Than_Operator = 154
    Match_Greater_Than_Or_Equal_Operator = 155
    Sll_Operator = 156
    Sla_Operator = 157
    Srl_Operator = 158
    Sra_Operator = 159
    Rol_Operator = 160
    Ror_Operator = 161
    Addition_Operator = 162
    Substraction_Operator = 163
    Concatenation_Operator = 164
    Multiplication_Operator = 165
    Division_Operator = 166
    Modulus_Operator = 167
    Remainder_Operator = 168
    Exponentiation_Operator = 169
    Function_Call = 170
    Aggregate = 171
    Parenthesis_Expression = 172
    Qualified_Expression = 173
    Type_Conversion = 174
    Allocator_By_Expression = 175
    Allocator_By_Subtype = 176
    Selected_Element = 177
    Dereference = 178
    Implicit_Dereference = 179
    Slice_Name = 180
    Indexed_Name = 181
    Psl_Expression = 182
    Sensitized_Process_Statement = 183
    Process_Statement = 184
    Concurrent_Simple_Signal_Assignment = 185
    Concurrent_Conditional_Signal_Assignment = 186
    Concurrent_Selected_Signal_Assignment = 187
    Concurrent_Assertion_Statement = 188
    Concurrent_Procedure_Call_Statement = 189
    Psl_Assert_Directive = 190
    Psl_Assume_Directive = 191
    Psl_Cover_Directive = 192
    Psl_Restrict_Directive = 193
    Block_Statement = 194
    If_Generate_Statement = 195
    Case_Generate_Statement = 196
    For_Generate_Statement = 197
    Component_Instantiation_Statement = 198
    Psl_Default_Clock = 199
    Simple_Simultaneous_Statement = 200
    Generate_Statement_Body = 201
    If_Generate_Else_Clause = 202
    Simple_Signal_Assignment_Statement = 203
    Conditional_Signal_Assignment_Statement = 204
    Selected_Waveform_Assignment_Statement = 205
    Null_Statement = 206
    Assertion_Statement = 207
    Report_Statement = 208
    Wait_Statement = 209
    Variable_Assignment_Statement = 210
    Conditional_Variable_Assignment_Statement = 211
    Return_Statement = 212
    For_Loop_Statement = 213
    While_Loop_Statement = 214
    Next_Statement = 215
    Exit_Statement = 216
    Case_Statement = 217
    Procedure_Call_Statement = 218
    If_Statement = 219
    Elsif = 220
    Character_Literal = 221
    Simple_Name = 222
    Selected_Name = 223
    Operator_Symbol = 224
    Reference_Name = 225
    External_Constant_Name = 226
    External_Signal_Name = 227
    External_Variable_Name = 228
    Selected_By_All_Name = 229
    Parenthesis_Name = 230
    Package_Pathname = 231
    Absolute_Pathname = 232
    Relative_Pathname = 233
    Pathname_Element = 234
    Base_Attribute = 235
    Subtype_Attribute = 236
    Element_Attribute = 237
    Left_Type_Attribute = 238
    Right_Type_Attribute = 239
    High_Type_Attribute = 240
    Low_Type_Attribute = 241
    Ascending_Type_Attribute = 242
    Image_Attribute = 243
    Value_Attribute = 244
    Pos_Attribute = 245
    Val_Attribute = 246
    Succ_Attribute = 247
    Pred_Attribute = 248
    Leftof_Attribute = 249
    Rightof_Attribute = 250
    Delayed_Attribute = 251
    Stable_Attribute = 252
    Quiet_Attribute = 253
    Transaction_Attribute = 254
    Event_Attribute = 255
    Active_Attribute = 256
    Last_Event_Attribute = 257
    Last_Active_Attribute = 258
    Last_Value_Attribute = 259
    Driving_Attribute = 260
    Driving_Value_Attribute = 261
    Behavior_Attribute = 262
    Structure_Attribute = 263
    Simple_Name_Attribute = 264
    Instance_Name_Attribute = 265
    Path_Name_Attribute = 266
    Left_Array_Attribute = 267
    Right_Array_Attribute = 268
    High_Array_Attribute = 269
    Low_Array_Attribute = 270
    Length_Array_Attribute = 271
    Ascending_Array_Attribute = 272
    Range_Array_Attribute = 273
    Reverse_Range_Array_Attribute = 274
    Attribute_Name = 275


class Iir_Kinds:
    Variable_Assignment_Statement = [
        Iir_Kind.Variable_Assignment_Statement,
        Iir_Kind.Conditional_Variable_Assignment_Statement]

    Case_Choice = [
        Iir_Kind.Choice_By_Range,
        Iir_Kind.Choice_By_Expression,
        Iir_Kind.Choice_By_Others]

    Array_Type_Definition = [
        Iir_Kind.Array_Type_Definition,
        Iir_Kind.Array_Subtype_Definition]

    Library_Unit = [
        Iir_Kind.Entity_Declaration,
        Iir_Kind.Configuration_Declaration,
        Iir_Kind.Context_Declaration,
        Iir_Kind.Package_Declaration,
        Iir_Kind.Package_Instantiation_Declaration,
        Iir_Kind.Vmode_Declaration,
        Iir_Kind.Vprop_Declaration,
        Iir_Kind.Vunit_Declaration,
        Iir_Kind.Package_Body,
        Iir_Kind.Architecture_Body]

    Array_Choice = [
        Iir_Kind.Choice_By_Range,
        Iir_Kind.Choice_By_Expression,
        Iir_Kind.Choice_By_Others,
        Iir_Kind.Choice_By_None]

    Subprogram_Declaration = [
        Iir_Kind.Function_Declaration,
        Iir_Kind.Procedure_Declaration]

    Subtype_Attribute = [
        Iir_Kind.Base_Attribute,
        Iir_Kind.Subtype_Attribute,
        Iir_Kind.Element_Attribute]

    Scalar_Subtype_Definition = [
        Iir_Kind.Physical_Subtype_Definition,
        Iir_Kind.Floating_Subtype_Definition,
        Iir_Kind.Integer_Subtype_Definition,
        Iir_Kind.Enumeration_Subtype_Definition]

    Nonoverloadable_Declaration = [
        Iir_Kind.Type_Declaration,
        Iir_Kind.Anonymous_Type_Declaration,
        Iir_Kind.Subtype_Declaration,
        Iir_Kind.Nature_Declaration,
        Iir_Kind.Subnature_Declaration,
        Iir_Kind.Package_Header,
        Iir_Kind.Unit_Declaration,
        Iir_Kind.Library_Declaration,
        Iir_Kind.Component_Declaration,
        Iir_Kind.Attribute_Declaration,
        Iir_Kind.Group_Template_Declaration,
        Iir_Kind.Group_Declaration,
        Iir_Kind.Element_Declaration]

    Literal = [
        Iir_Kind.Integer_Literal,
        Iir_Kind.Floating_Point_Literal,
        Iir_Kind.Null_Literal,
        Iir_Kind.String_Literal8,
        Iir_Kind.Physical_Int_Literal,
        Iir_Kind.Physical_Fp_Literal]

    Process_Statement = [
        Iir_Kind.Sensitized_Process_Statement,
        Iir_Kind.Process_Statement]

    Object_Declaration = [
        Iir_Kind.Object_Alias_Declaration,
        Iir_Kind.File_Declaration,
        Iir_Kind.Guard_Signal_Declaration,
        Iir_Kind.Signal_Declaration,
        Iir_Kind.Variable_Declaration,
        Iir_Kind.Constant_Declaration,
        Iir_Kind.Iterator_Declaration,
        Iir_Kind.Interface_Constant_Declaration,
        Iir_Kind.Interface_Variable_Declaration,
        Iir_Kind.Interface_Signal_Declaration,
        Iir_Kind.Interface_File_Declaration]

    Clause = [
        Iir_Kind.Library_Clause,
        Iir_Kind.Use_Clause,
        Iir_Kind.Context_Reference]

    Type_And_Subtype_Definition = [
        Iir_Kind.Access_Type_Definition,
        Iir_Kind.Incomplete_Type_Definition,
        Iir_Kind.Interface_Type_Definition,
        Iir_Kind.File_Type_Definition,
        Iir_Kind.Protected_Type_Declaration,
        Iir_Kind.Record_Type_Definition,
        Iir_Kind.Array_Type_Definition,
        Iir_Kind.Array_Subtype_Definition,
        Iir_Kind.Record_Subtype_Definition,
        Iir_Kind.Access_Subtype_Definition,
        Iir_Kind.Physical_Subtype_Definition,
        Iir_Kind.Floating_Subtype_Definition,
        Iir_Kind.Integer_Subtype_Definition,
        Iir_Kind.Enumeration_Subtype_Definition,
        Iir_Kind.Enumeration_Type_Definition,
        Iir_Kind.Integer_Type_Definition,
        Iir_Kind.Floating_Type_Definition,
        Iir_Kind.Physical_Type_Definition]

    External_Name = [
        Iir_Kind.External_Constant_Name,
        Iir_Kind.External_Signal_Name,
        Iir_Kind.External_Variable_Name]

    Primary_Unit = [
        Iir_Kind.Entity_Declaration,
        Iir_Kind.Configuration_Declaration,
        Iir_Kind.Context_Declaration,
        Iir_Kind.Package_Declaration,
        Iir_Kind.Package_Instantiation_Declaration,
        Iir_Kind.Vmode_Declaration,
        Iir_Kind.Vprop_Declaration,
        Iir_Kind.Vunit_Declaration]

    Record_Choice = [
        Iir_Kind.Choice_By_Others,
        Iir_Kind.Choice_By_None,
        Iir_Kind.Choice_By_Name]

    Functions_And_Literals = [
        Iir_Kind.Enumeration_Literal,
        Iir_Kind.Function_Declaration]

    Verification_Unit = [
        Iir_Kind.Vmode_Declaration,
        Iir_Kind.Vprop_Declaration,
        Iir_Kind.Vunit_Declaration]

    Secondary_Unit = [
        Iir_Kind.Package_Body,
        Iir_Kind.Architecture_Body]

    Package_Declaration = [
        Iir_Kind.Package_Declaration,
        Iir_Kind.Package_Instantiation_Declaration]

    Dereference = [
        Iir_Kind.Dereference,
        Iir_Kind.Implicit_Dereference]

    Composite_Subtype_Definition = [
        Iir_Kind.Array_Subtype_Definition,
        Iir_Kind.Record_Subtype_Definition]

    Choice = [
        Iir_Kind.Choice_By_Range,
        Iir_Kind.Choice_By_Expression,
        Iir_Kind.Choice_By_Others,
        Iir_Kind.Choice_By_None,
        Iir_Kind.Choice_By_Name]

    If_Case_Generate_Statement = [
        Iir_Kind.If_Generate_Statement,
        Iir_Kind.Case_Generate_Statement]

    Simple_Concurrent_Statement = [
        Iir_Kind.Sensitized_Process_Statement,
        Iir_Kind.Process_Statement,
        Iir_Kind.Concurrent_Simple_Signal_Assignment,
        Iir_Kind.Concurrent_Conditional_Signal_Assignment,
        Iir_Kind.Concurrent_Selected_Signal_Assignment,
        Iir_Kind.Concurrent_Assertion_Statement,
        Iir_Kind.Concurrent_Procedure_Call_Statement,
        Iir_Kind.Psl_Assert_Directive,
        Iir_Kind.Psl_Assume_Directive,
        Iir_Kind.Psl_Cover_Directive,
        Iir_Kind.Psl_Restrict_Directive]

    Non_Alias_Object_Declaration = [
        Iir_Kind.File_Declaration,
        Iir_Kind.Guard_Signal_Declaration,
        Iir_Kind.Signal_Declaration,
        Iir_Kind.Variable_Declaration,
        Iir_Kind.Constant_Declaration,
        Iir_Kind.Iterator_Declaration,
        Iir_Kind.Interface_Constant_Declaration,
        Iir_Kind.Interface_Variable_Declaration,
        Iir_Kind.Interface_Signal_Declaration,
        Iir_Kind.Interface_File_Declaration]

    Entity_Aspect = [
        Iir_Kind.Entity_Aspect_Entity,
        Iir_Kind.Entity_Aspect_Configuration,
        Iir_Kind.Entity_Aspect_Open]

    Subprogram_Body = [
        Iir_Kind.Function_Body,
        Iir_Kind.Procedure_Body]

    Type_Attribute = [
        Iir_Kind.Left_Type_Attribute,
        Iir_Kind.Right_Type_Attribute,
        Iir_Kind.High_Type_Attribute,
        Iir_Kind.Low_Type_Attribute,
        Iir_Kind.Ascending_Type_Attribute]

    Specification = [
        Iir_Kind.Attribute_Specification,
        Iir_Kind.Disconnection_Specification,
        Iir_Kind.Configuration_Specification]

    Dyadic_Operator = [
        Iir_Kind.And_Operator,
        Iir_Kind.Or_Operator,
        Iir_Kind.Nand_Operator,
        Iir_Kind.Nor_Operator,
        Iir_Kind.Xor_Operator,
        Iir_Kind.Xnor_Operator,
        Iir_Kind.Equality_Operator,
        Iir_Kind.Inequality_Operator,
        Iir_Kind.Less_Than_Operator,
        Iir_Kind.Less_Than_Or_Equal_Operator,
        Iir_Kind.Greater_Than_Operator,
        Iir_Kind.Greater_Than_Or_Equal_Operator,
        Iir_Kind.Match_Equality_Operator,
        Iir_Kind.Match_Inequality_Operator,
        Iir_Kind.Match_Less_Than_Operator,
        Iir_Kind.Match_Less_Than_Or_Equal_Operator,
        Iir_Kind.Match_Greater_Than_Operator,
        Iir_Kind.Match_Greater_Than_Or_Equal_Operator,
        Iir_Kind.Sll_Operator,
        Iir_Kind.Sla_Operator,
        Iir_Kind.Srl_Operator,
        Iir_Kind.Sra_Operator,
        Iir_Kind.Rol_Operator,
        Iir_Kind.Ror_Operator,
        Iir_Kind.Addition_Operator,
        Iir_Kind.Substraction_Operator,
        Iir_Kind.Concatenation_Operator,
        Iir_Kind.Multiplication_Operator,
        Iir_Kind.Division_Operator,
        Iir_Kind.Modulus_Operator,
        Iir_Kind.Remainder_Operator,
        Iir_Kind.Exponentiation_Operator]

    Expression_Attribute = [
        Iir_Kind.Left_Type_Attribute,
        Iir_Kind.Right_Type_Attribute,
        Iir_Kind.High_Type_Attribute,
        Iir_Kind.Low_Type_Attribute,
        Iir_Kind.Ascending_Type_Attribute,
        Iir_Kind.Image_Attribute,
        Iir_Kind.Value_Attribute,
        Iir_Kind.Pos_Attribute,
        Iir_Kind.Val_Attribute,
        Iir_Kind.Succ_Attribute,
        Iir_Kind.Pred_Attribute,
        Iir_Kind.Leftof_Attribute,
        Iir_Kind.Rightof_Attribute,
        Iir_Kind.Delayed_Attribute,
        Iir_Kind.Stable_Attribute,
        Iir_Kind.Quiet_Attribute,
        Iir_Kind.Transaction_Attribute,
        Iir_Kind.Event_Attribute,
        Iir_Kind.Active_Attribute,
        Iir_Kind.Last_Event_Attribute,
        Iir_Kind.Last_Active_Attribute,
        Iir_Kind.Last_Value_Attribute,
        Iir_Kind.Driving_Attribute,
        Iir_Kind.Driving_Value_Attribute,
        Iir_Kind.Behavior_Attribute,
        Iir_Kind.Structure_Attribute,
        Iir_Kind.Simple_Name_Attribute,
        Iir_Kind.Instance_Name_Attribute,
        Iir_Kind.Path_Name_Attribute,
        Iir_Kind.Left_Array_Attribute,
        Iir_Kind.Right_Array_Attribute,
        Iir_Kind.High_Array_Attribute,
        Iir_Kind.Low_Array_Attribute,
        Iir_Kind.Length_Array_Attribute,
        Iir_Kind.Ascending_Array_Attribute]

    Monadic_Operator = [
        Iir_Kind.Identity_Operator,
        Iir_Kind.Negation_Operator,
        Iir_Kind.Absolute_Operator,
        Iir_Kind.Not_Operator,
        Iir_Kind.Implicit_Condition_Operator,
        Iir_Kind.Condition_Operator,
        Iir_Kind.Reduction_And_Operator,
        Iir_Kind.Reduction_Or_Operator,
        Iir_Kind.Reduction_Nand_Operator,
        Iir_Kind.Reduction_Nor_Operator,
        Iir_Kind.Reduction_Xor_Operator,
        Iir_Kind.Reduction_Xnor_Operator]

    Interface_Declaration = [
        Iir_Kind.Interface_Constant_Declaration,
        Iir_Kind.Interface_Variable_Declaration,
        Iir_Kind.Interface_Signal_Declaration,
        Iir_Kind.Interface_File_Declaration,
        Iir_Kind.Interface_Type_Declaration,
        Iir_Kind.Interface_Package_Declaration,
        Iir_Kind.Interface_Function_Declaration,
        Iir_Kind.Interface_Procedure_Declaration]

    Array_Attribute = [
        Iir_Kind.Left_Array_Attribute,
        Iir_Kind.Right_Array_Attribute,
        Iir_Kind.High_Array_Attribute,
        Iir_Kind.Low_Array_Attribute,
        Iir_Kind.Length_Array_Attribute,
        Iir_Kind.Ascending_Array_Attribute,
        Iir_Kind.Range_Array_Attribute,
        Iir_Kind.Reverse_Range_Array_Attribute]

    Sequential_Statement = [
        Iir_Kind.Simple_Signal_Assignment_Statement,
        Iir_Kind.Conditional_Signal_Assignment_Statement,
        Iir_Kind.Selected_Waveform_Assignment_Statement,
        Iir_Kind.Null_Statement,
        Iir_Kind.Assertion_Statement,
        Iir_Kind.Report_Statement,
        Iir_Kind.Wait_Statement,
        Iir_Kind.Variable_Assignment_Statement,
        Iir_Kind.Conditional_Variable_Assignment_Statement,
        Iir_Kind.Return_Statement,
        Iir_Kind.For_Loop_Statement,
        Iir_Kind.While_Loop_Statement,
        Iir_Kind.Next_Statement,
        Iir_Kind.Exit_Statement,
        Iir_Kind.Case_Statement,
        Iir_Kind.Procedure_Call_Statement,
        Iir_Kind.If_Statement]

    Denoting_And_External_Name = [
        Iir_Kind.Character_Literal,
        Iir_Kind.Simple_Name,
        Iir_Kind.Selected_Name,
        Iir_Kind.Operator_Symbol,
        Iir_Kind.Reference_Name,
        Iir_Kind.External_Constant_Name,
        Iir_Kind.External_Signal_Name,
        Iir_Kind.External_Variable_Name]

    Range_Type_Definition = [
        Iir_Kind.Physical_Subtype_Definition,
        Iir_Kind.Floating_Subtype_Definition,
        Iir_Kind.Integer_Subtype_Definition,
        Iir_Kind.Enumeration_Subtype_Definition,
        Iir_Kind.Enumeration_Type_Definition]

    Discrete_Type_Definition = [
        Iir_Kind.Integer_Subtype_Definition,
        Iir_Kind.Enumeration_Subtype_Definition,
        Iir_Kind.Enumeration_Type_Definition,
        Iir_Kind.Integer_Type_Definition]

    Concurrent_Statement = [
        Iir_Kind.Sensitized_Process_Statement,
        Iir_Kind.Process_Statement,
        Iir_Kind.Concurrent_Simple_Signal_Assignment,
        Iir_Kind.Concurrent_Conditional_Signal_Assignment,
        Iir_Kind.Concurrent_Selected_Signal_Assignment,
        Iir_Kind.Concurrent_Assertion_Statement,
        Iir_Kind.Concurrent_Procedure_Call_Statement,
        Iir_Kind.Psl_Assert_Directive,
        Iir_Kind.Psl_Assume_Directive,
        Iir_Kind.Psl_Cover_Directive,
        Iir_Kind.Psl_Restrict_Directive,
        Iir_Kind.Block_Statement,
        Iir_Kind.If_Generate_Statement,
        Iir_Kind.Case_Generate_Statement,
        Iir_Kind.For_Generate_Statement,
        Iir_Kind.Component_Instantiation_Statement,
        Iir_Kind.Psl_Default_Clock]

    Signal_Attribute = [
        Iir_Kind.Delayed_Attribute,
        Iir_Kind.Stable_Attribute,
        Iir_Kind.Quiet_Attribute,
        Iir_Kind.Transaction_Attribute]

    Type_Declaration = [
        Iir_Kind.Type_Declaration,
        Iir_Kind.Anonymous_Type_Declaration,
        Iir_Kind.Subtype_Declaration]

    Association_Element = [
        Iir_Kind.Association_Element_By_Expression,
        Iir_Kind.Association_Element_By_Individual,
        Iir_Kind.Association_Element_Open]

    Interface_Object_Declaration = [
        Iir_Kind.Interface_Constant_Declaration,
        Iir_Kind.Interface_Variable_Declaration,
        Iir_Kind.Interface_Signal_Declaration,
        Iir_Kind.Interface_File_Declaration]

    Composite_Type_Definition = [
        Iir_Kind.Record_Type_Definition,
        Iir_Kind.Array_Type_Definition,
        Iir_Kind.Array_Subtype_Definition,
        Iir_Kind.Record_Subtype_Definition]

    Interface_Subprogram_Declaration = [
        Iir_Kind.Interface_Function_Declaration,
        Iir_Kind.Interface_Procedure_Declaration]

    Branch_Quantity_Declaration = [
        Iir_Kind.Across_Quantity_Declaration,
        Iir_Kind.Through_Quantity_Declaration]

    Signal_Value_Attribute = [
        Iir_Kind.Event_Attribute,
        Iir_Kind.Active_Attribute,
        Iir_Kind.Last_Event_Attribute,
        Iir_Kind.Last_Active_Attribute,
        Iir_Kind.Last_Value_Attribute,
        Iir_Kind.Driving_Attribute,
        Iir_Kind.Driving_Value_Attribute]

    Quantity_Declaration = [
        Iir_Kind.Free_Quantity_Declaration,
        Iir_Kind.Across_Quantity_Declaration,
        Iir_Kind.Through_Quantity_Declaration]

    Physical_Literal = [
        Iir_Kind.Physical_Int_Literal,
        Iir_Kind.Physical_Fp_Literal]

    Scalar_Type_And_Subtype_Definition = [
        Iir_Kind.Physical_Subtype_Definition,
        Iir_Kind.Floating_Subtype_Definition,
        Iir_Kind.Integer_Subtype_Definition,
        Iir_Kind.Enumeration_Subtype_Definition,
        Iir_Kind.Enumeration_Type_Definition,
        Iir_Kind.Integer_Type_Definition,
        Iir_Kind.Floating_Type_Definition,
        Iir_Kind.Physical_Type_Definition]

    Attribute = [
        Iir_Kind.Base_Attribute,
        Iir_Kind.Subtype_Attribute,
        Iir_Kind.Element_Attribute,
        Iir_Kind.Left_Type_Attribute,
        Iir_Kind.Right_Type_Attribute,
        Iir_Kind.High_Type_Attribute,
        Iir_Kind.Low_Type_Attribute,
        Iir_Kind.Ascending_Type_Attribute,
        Iir_Kind.Image_Attribute,
        Iir_Kind.Value_Attribute,
        Iir_Kind.Pos_Attribute,
        Iir_Kind.Val_Attribute,
        Iir_Kind.Succ_Attribute,
        Iir_Kind.Pred_Attribute,
        Iir_Kind.Leftof_Attribute,
        Iir_Kind.Rightof_Attribute,
        Iir_Kind.Delayed_Attribute,
        Iir_Kind.Stable_Attribute,
        Iir_Kind.Quiet_Attribute,
        Iir_Kind.Transaction_Attribute,
        Iir_Kind.Event_Attribute,
        Iir_Kind.Active_Attribute,
        Iir_Kind.Last_Event_Attribute,
        Iir_Kind.Last_Active_Attribute,
        Iir_Kind.Last_Value_Attribute,
        Iir_Kind.Driving_Attribute,
        Iir_Kind.Driving_Value_Attribute,
        Iir_Kind.Behavior_Attribute,
        Iir_Kind.Structure_Attribute,
        Iir_Kind.Simple_Name_Attribute,
        Iir_Kind.Instance_Name_Attribute,
        Iir_Kind.Path_Name_Attribute,
        Iir_Kind.Left_Array_Attribute,
        Iir_Kind.Right_Array_Attribute,
        Iir_Kind.High_Array_Attribute,
        Iir_Kind.Low_Array_Attribute,
        Iir_Kind.Length_Array_Attribute,
        Iir_Kind.Ascending_Array_Attribute,
        Iir_Kind.Range_Array_Attribute,
        Iir_Kind.Reverse_Range_Array_Attribute]

    Denoting_Name = [
        Iir_Kind.Character_Literal,
        Iir_Kind.Simple_Name,
        Iir_Kind.Selected_Name,
        Iir_Kind.Operator_Symbol,
        Iir_Kind.Reference_Name]

    Concurrent_Signal_Assignment = [
        Iir_Kind.Concurrent_Simple_Signal_Assignment,
        Iir_Kind.Concurrent_Conditional_Signal_Assignment,
        Iir_Kind.Concurrent_Selected_Signal_Assignment]

    Range_Attribute = [
        Iir_Kind.Range_Array_Attribute,
        Iir_Kind.Reverse_Range_Array_Attribute]

    Name_Attribute = [
        Iir_Kind.Simple_Name_Attribute,
        Iir_Kind.Instance_Name_Attribute,
        Iir_Kind.Path_Name_Attribute]

    Scalar_Type_Attribute = [
        Iir_Kind.Pos_Attribute,
        Iir_Kind.Val_Attribute,
        Iir_Kind.Succ_Attribute,
        Iir_Kind.Pred_Attribute,
        Iir_Kind.Leftof_Attribute,
        Iir_Kind.Rightof_Attribute]

    Name = [
        Iir_Kind.Character_Literal,
        Iir_Kind.Simple_Name,
        Iir_Kind.Selected_Name,
        Iir_Kind.Operator_Symbol,
        Iir_Kind.Reference_Name,
        Iir_Kind.External_Constant_Name,
        Iir_Kind.External_Signal_Name,
        Iir_Kind.External_Variable_Name,
        Iir_Kind.Selected_By_All_Name,
        Iir_Kind.Parenthesis_Name]

    Subtype_Definition = [
        Iir_Kind.Array_Subtype_Definition,
        Iir_Kind.Record_Subtype_Definition,
        Iir_Kind.Access_Subtype_Definition,
        Iir_Kind.Physical_Subtype_Definition,
        Iir_Kind.Floating_Subtype_Definition,
        Iir_Kind.Integer_Subtype_Definition,
        Iir_Kind.Enumeration_Subtype_Definition]

    Allocator = [
        Iir_Kind.Allocator_By_Expression,
        Iir_Kind.Allocator_By_Subtype]



class Iir_Mode:
    Unknown_Mode = 0
    Linkage_Mode = 1
    Buffer_Mode = 2
    Out_Mode = 3
    Inout_Mode = 4
    In_Mode = 5


class Iir_Staticness:
    Unknown = 0
    PNone = 1
    Globally = 2
    Locally = 3


class Iir_Constraint:
    Unconstrained = 0
    Partially_Constrained = 1
    Fully_Constrained = 2


class Iir_Direction:
    To = 0
    Downto = 1


class Iir_Delay_Mechanism:
    Inertial_Delay = 0
    Transport_Delay = 1


class Date_State:
    Extern = 0
    Disk = 1
    Parse = 2
    Analyze = 3


class Iir_Predefined:
    Error = 0
    Boolean_And = 1
    Boolean_Or = 2
    Boolean_Nand = 3
    Boolean_Nor = 4
    Boolean_Xor = 5
    Boolean_Xnor = 6
    Boolean_Not = 7
    Boolean_Rising_Edge = 8
    Boolean_Falling_Edge = 9
    Enum_Equality = 10
    Enum_Inequality = 11
    Enum_Less = 12
    Enum_Less_Equal = 13
    Enum_Greater = 14
    Enum_Greater_Equal = 15
    Enum_Minimum = 16
    Enum_Maximum = 17
    Enum_To_String = 18
    Bit_And = 19
    Bit_Or = 20
    Bit_Nand = 21
    Bit_Nor = 22
    Bit_Xor = 23
    Bit_Xnor = 24
    Bit_Not = 25
    Bit_Match_Equality = 26
    Bit_Match_Inequality = 27
    Bit_Match_Less = 28
    Bit_Match_Less_Equal = 29
    Bit_Match_Greater = 30
    Bit_Match_Greater_Equal = 31
    Bit_Condition = 32
    Bit_Rising_Edge = 33
    Bit_Falling_Edge = 34
    Integer_Equality = 35
    Integer_Inequality = 36
    Integer_Less = 37
    Integer_Less_Equal = 38
    Integer_Greater = 39
    Integer_Greater_Equal = 40
    Integer_Identity = 41
    Integer_Negation = 42
    Integer_Absolute = 43
    Integer_Plus = 44
    Integer_Minus = 45
    Integer_Mul = 46
    Integer_Div = 47
    Integer_Mod = 48
    Integer_Rem = 49
    Integer_Exp = 50
    Integer_Minimum = 51
    Integer_Maximum = 52
    Integer_To_String = 53
    Floating_Equality = 54
    Floating_Inequality = 55
    Floating_Less = 56
    Floating_Less_Equal = 57
    Floating_Greater = 58
    Floating_Greater_Equal = 59
    Floating_Identity = 60
    Floating_Negation = 61
    Floating_Absolute = 62
    Floating_Plus = 63
    Floating_Minus = 64
    Floating_Mul = 65
    Floating_Div = 66
    Floating_Exp = 67
    Floating_Minimum = 68
    Floating_Maximum = 69
    Floating_To_String = 70
    Real_To_String_Digits = 71
    Real_To_String_Format = 72
    Universal_R_I_Mul = 73
    Universal_I_R_Mul = 74
    Universal_R_I_Div = 75
    Physical_Equality = 76
    Physical_Inequality = 77
    Physical_Less = 78
    Physical_Less_Equal = 79
    Physical_Greater = 80
    Physical_Greater_Equal = 81
    Physical_Identity = 82
    Physical_Negation = 83
    Physical_Absolute = 84
    Physical_Plus = 85
    Physical_Minus = 86
    Physical_Integer_Mul = 87
    Physical_Real_Mul = 88
    Integer_Physical_Mul = 89
    Real_Physical_Mul = 90
    Physical_Integer_Div = 91
    Physical_Real_Div = 92
    Physical_Physical_Div = 93
    Physical_Minimum = 94
    Physical_Maximum = 95
    Physical_To_String = 96
    Time_To_String_Unit = 97
    Access_Equality = 98
    Access_Inequality = 99
    Record_Equality = 100
    Record_Inequality = 101
    Array_Equality = 102
    Array_Inequality = 103
    Array_Less = 104
    Array_Less_Equal = 105
    Array_Greater = 106
    Array_Greater_Equal = 107
    Array_Array_Concat = 108
    Array_Element_Concat = 109
    Element_Array_Concat = 110
    Element_Element_Concat = 111
    Array_Minimum = 112
    Array_Maximum = 113
    Vector_Minimum = 114
    Vector_Maximum = 115
    Array_Sll = 116
    Array_Srl = 117
    Array_Sla = 118
    Array_Sra = 119
    Array_Rol = 120
    Array_Ror = 121
    TF_Array_And = 122
    TF_Array_Or = 123
    TF_Array_Nand = 124
    TF_Array_Nor = 125
    TF_Array_Xor = 126
    TF_Array_Xnor = 127
    TF_Array_Not = 128
    TF_Reduction_And = 129
    TF_Reduction_Or = 130
    TF_Reduction_Nand = 131
    TF_Reduction_Nor = 132
    TF_Reduction_Xor = 133
    TF_Reduction_Xnor = 134
    TF_Reduction_Not = 135
    TF_Array_Element_And = 136
    TF_Element_Array_And = 137
    TF_Array_Element_Or = 138
    TF_Element_Array_Or = 139
    TF_Array_Element_Nand = 140
    TF_Element_Array_Nand = 141
    TF_Array_Element_Nor = 142
    TF_Element_Array_Nor = 143
    TF_Array_Element_Xor = 144
    TF_Element_Array_Xor = 145
    TF_Array_Element_Xnor = 146
    TF_Element_Array_Xnor = 147
    Bit_Array_Match_Equality = 148
    Bit_Array_Match_Inequality = 149
    Array_Char_To_String = 150
    Bit_Vector_To_Ostring = 151
    Bit_Vector_To_Hstring = 152
    Std_Ulogic_Match_Equality = 153
    Std_Ulogic_Match_Inequality = 154
    Std_Ulogic_Match_Less = 155
    Std_Ulogic_Match_Less_Equal = 156
    Std_Ulogic_Match_Greater = 157
    Std_Ulogic_Match_Greater_Equal = 158
    Std_Ulogic_Array_Match_Equality = 159
    Std_Ulogic_Array_Match_Inequality = 160
    Deallocate = 161
    File_Open = 162
    File_Open_Status = 163
    File_Close = 164
    Read = 165
    Read_Length = 166
    Flush = 167
    Write = 168
    Endfile = 169
    Now_Function = 170
    PNone = 171
    Ieee_1164_Scalar_And = 172
    Ieee_1164_Scalar_Nand = 173
    Ieee_1164_Scalar_Or = 174
    Ieee_1164_Scalar_Nor = 175
    Ieee_1164_Scalar_Xor = 176
    Ieee_1164_Scalar_Xnor = 177
    Ieee_1164_Scalar_Not = 178
    Ieee_1164_Vector_And = 179
    Ieee_1164_Vector_Nand = 180
    Ieee_1164_Vector_Or = 181
    Ieee_1164_Vector_Nor = 182
    Ieee_1164_Vector_Xor = 183
    Ieee_1164_Vector_Xnor = 184
    Ieee_1164_Vector_Not = 185
    Ieee_Numeric_Std_Toint_Uns_Nat = 186
    Ieee_Numeric_Std_Toint_Sgn_Int = 187
    Ieee_Numeric_Std_Touns_Nat_Nat_Uns = 188
    Ieee_Numeric_Std_Touns_Nat_Uns_Uns = 189
    Ieee_Numeric_Std_Tosgn_Int_Nat_Sgn = 190
    Ieee_Numeric_Std_Tosgn_Int_Sgn_Sgn = 191
    Ieee_Numeric_Std_Resize_Uns_Nat = 192
    Ieee_Numeric_Std_Resize_Sgn_Nat = 193
    Ieee_Numeric_Std_Resize_Uns_Uns = 194
    Ieee_Numeric_Std_Resize_Sgn_Sgn = 195
    Ieee_Numeric_Std_Add_Uns_Uns = 196
    Ieee_Numeric_Std_Add_Uns_Nat = 197
    Ieee_Numeric_Std_Add_Nat_Uns = 198
    Ieee_Numeric_Std_Add_Sgn_Sgn = 199
    Ieee_Numeric_Std_Add_Sgn_Int = 200
    Ieee_Numeric_Std_Add_Int_Sgn = 201
    Ieee_Numeric_Std_Sub_Uns_Uns = 202
    Ieee_Numeric_Std_Sub_Uns_Nat = 203
    Ieee_Numeric_Std_Sub_Nat_Uns = 204
    Ieee_Numeric_Std_Sub_Sgn_Sgn = 205
    Ieee_Numeric_Std_Sub_Sgn_Int = 206
    Ieee_Numeric_Std_Sub_Int_Sgn = 207
    Ieee_Numeric_Std_Gt_Uns_Uns = 208
    Ieee_Numeric_Std_Gt_Uns_Nat = 209
    Ieee_Numeric_Std_Gt_Nat_Uns = 210
    Ieee_Numeric_Std_Gt_Sgn_Sgn = 211
    Ieee_Numeric_Std_Gt_Sgn_Int = 212
    Ieee_Numeric_Std_Gt_Int_Sgn = 213
    Ieee_Numeric_Std_Lt_Uns_Uns = 214
    Ieee_Numeric_Std_Lt_Uns_Nat = 215
    Ieee_Numeric_Std_Lt_Nat_Uns = 216
    Ieee_Numeric_Std_Lt_Sgn_Sgn = 217
    Ieee_Numeric_Std_Lt_Sgn_Int = 218
    Ieee_Numeric_Std_Lt_Int_Sgn = 219
    Ieee_Numeric_Std_Le_Uns_Uns = 220
    Ieee_Numeric_Std_Le_Uns_Nat = 221
    Ieee_Numeric_Std_Le_Nat_Uns = 222
    Ieee_Numeric_Std_Le_Sgn_Sgn = 223
    Ieee_Numeric_Std_Le_Sgn_Int = 224
    Ieee_Numeric_Std_Le_Int_Sgn = 225
    Ieee_Numeric_Std_Ge_Uns_Uns = 226
    Ieee_Numeric_Std_Ge_Uns_Nat = 227
    Ieee_Numeric_Std_Ge_Nat_Uns = 228
    Ieee_Numeric_Std_Ge_Sgn_Sgn = 229
    Ieee_Numeric_Std_Ge_Sgn_Int = 230
    Ieee_Numeric_Std_Ge_Int_Sgn = 231
    Ieee_Numeric_Std_Eq_Uns_Uns = 232
    Ieee_Numeric_Std_Eq_Uns_Nat = 233
    Ieee_Numeric_Std_Eq_Nat_Uns = 234
    Ieee_Numeric_Std_Eq_Sgn_Sgn = 235
    Ieee_Numeric_Std_Eq_Sgn_Int = 236
    Ieee_Numeric_Std_Eq_Int_Sgn = 237
    Ieee_Numeric_Std_Ne_Uns_Uns = 238
    Ieee_Numeric_Std_Ne_Uns_Nat = 239
    Ieee_Numeric_Std_Ne_Nat_Uns = 240
    Ieee_Numeric_Std_Ne_Sgn_Sgn = 241
    Ieee_Numeric_Std_Ne_Sgn_Int = 242
    Ieee_Numeric_Std_Ne_Int_Sgn = 243
    Ieee_Numeric_Std_Not_Uns = 244
    Ieee_Numeric_Std_Not_Sgn = 245
    Ieee_Numeric_Std_And_Uns_Uns = 246
    Ieee_Numeric_Std_And_Sgn_Sgn = 247
    Ieee_Numeric_Std_Or_Uns_Uns = 248
    Ieee_Numeric_Std_Or_Sgn_Sgn = 249
    Ieee_Numeric_Std_Nand_Uns_Uns = 250
    Ieee_Numeric_Std_Nand_Sgn_Sgn = 251
    Ieee_Numeric_Std_Nor_Uns_Uns = 252
    Ieee_Numeric_Std_Nor_Sgn_Sgn = 253
    Ieee_Numeric_Std_Xor_Uns_Uns = 254
    Ieee_Numeric_Std_Xor_Sgn_Sgn = 255
    Ieee_Numeric_Std_Xnor_Uns_Uns = 256
    Ieee_Numeric_Std_Xnor_Sgn_Sgn = 257
    Ieee_Numeric_Std_Neg_Uns = 258
    Ieee_Numeric_Std_Neg_Sgn = 259
    Ieee_Math_Real_Ceil = 260
    Ieee_Math_Real_Log2 = 261
    Ieee_Std_Logic_Unsigned_Add_Slv_Slv = 262
    Ieee_Std_Logic_Unsigned_Add_Slv_Int = 263
    Ieee_Std_Logic_Unsigned_Add_Int_Slv = 264
    Ieee_Std_Logic_Unsigned_Add_Slv_Sl = 265
    Ieee_Std_Logic_Unsigned_Add_Sl_Slv = 266
    Ieee_Std_Logic_Unsigned_Lt_Slv_Slv = 267
    Ieee_Std_Logic_Unsigned_Lt_Slv_Int = 268
    Ieee_Std_Logic_Unsigned_Lt_Int_Slv = 269
    Ieee_Std_Logic_Unsigned_Le_Slv_Slv = 270
    Ieee_Std_Logic_Unsigned_Le_Slv_Int = 271
    Ieee_Std_Logic_Unsigned_Le_Int_Slv = 272
    Ieee_Std_Logic_Unsigned_Gt_Slv_Slv = 273
    Ieee_Std_Logic_Unsigned_Gt_Slv_Int = 274
    Ieee_Std_Logic_Unsigned_Gt_Int_Slv = 275
    Ieee_Std_Logic_Unsigned_Ge_Slv_Slv = 276
    Ieee_Std_Logic_Unsigned_Ge_Slv_Int = 277
    Ieee_Std_Logic_Unsigned_Ge_Int_Slv = 278
    Ieee_Std_Logic_Unsigned_Eq_Slv_Slv = 279
    Ieee_Std_Logic_Unsigned_Eq_Slv_Int = 280
    Ieee_Std_Logic_Unsigned_Eq_Int_Slv = 281
    Ieee_Std_Logic_Unsigned_Ne_Slv_Slv = 282
    Ieee_Std_Logic_Unsigned_Ne_Slv_Int = 283
    Ieee_Std_Logic_Unsigned_Ne_Int_Slv = 284

Get_Kind = libghdl.vhdl__nodes__get_kind
Get_Location = libghdl.vhdl__nodes__get_location

Get_First_Design_Unit = libghdl.vhdl__nodes__get_first_design_unit

Set_First_Design_Unit = libghdl.vhdl__nodes__set_first_design_unit

Get_Last_Design_Unit = libghdl.vhdl__nodes__get_last_design_unit

Set_Last_Design_Unit = libghdl.vhdl__nodes__set_last_design_unit

Get_Library_Declaration = libghdl.vhdl__nodes__get_library_declaration

Set_Library_Declaration = libghdl.vhdl__nodes__set_library_declaration

Get_File_Checksum = libghdl.vhdl__nodes__get_file_checksum

Set_File_Checksum = libghdl.vhdl__nodes__set_file_checksum

Get_Analysis_Time_Stamp = libghdl.vhdl__nodes__get_analysis_time_stamp

Set_Analysis_Time_Stamp = libghdl.vhdl__nodes__set_analysis_time_stamp

Get_Design_File_Source = libghdl.vhdl__nodes__get_design_file_source

Set_Design_File_Source = libghdl.vhdl__nodes__set_design_file_source

Get_Library = libghdl.vhdl__nodes__get_library

Set_Library = libghdl.vhdl__nodes__set_library

Get_File_Dependence_List = libghdl.vhdl__nodes__get_file_dependence_list

Set_File_Dependence_List = libghdl.vhdl__nodes__set_file_dependence_list

Get_Design_File_Filename = libghdl.vhdl__nodes__get_design_file_filename

Set_Design_File_Filename = libghdl.vhdl__nodes__set_design_file_filename

Get_Design_File_Directory = libghdl.vhdl__nodes__get_design_file_directory

Set_Design_File_Directory = libghdl.vhdl__nodes__set_design_file_directory

Get_Design_File = libghdl.vhdl__nodes__get_design_file

Set_Design_File = libghdl.vhdl__nodes__set_design_file

Get_Design_File_Chain = libghdl.vhdl__nodes__get_design_file_chain

Set_Design_File_Chain = libghdl.vhdl__nodes__set_design_file_chain

Get_Library_Directory = libghdl.vhdl__nodes__get_library_directory

Set_Library_Directory = libghdl.vhdl__nodes__set_library_directory

Get_Date = libghdl.vhdl__nodes__get_date

Set_Date = libghdl.vhdl__nodes__set_date

Get_Context_Items = libghdl.vhdl__nodes__get_context_items

Set_Context_Items = libghdl.vhdl__nodes__set_context_items

Get_Dependence_List = libghdl.vhdl__nodes__get_dependence_list

Set_Dependence_List = libghdl.vhdl__nodes__set_dependence_list

Get_Analysis_Checks_List = libghdl.vhdl__nodes__get_analysis_checks_list

Set_Analysis_Checks_List = libghdl.vhdl__nodes__set_analysis_checks_list

Get_Date_State = libghdl.vhdl__nodes__get_date_state

Set_Date_State = libghdl.vhdl__nodes__set_date_state

Get_Guarded_Target_State = libghdl.vhdl__nodes__get_guarded_target_state

Set_Guarded_Target_State = libghdl.vhdl__nodes__set_guarded_target_state

Get_Library_Unit = libghdl.vhdl__nodes__get_library_unit

Set_Library_Unit = libghdl.vhdl__nodes__set_library_unit

Get_Hash_Chain = libghdl.vhdl__nodes__get_hash_chain

Set_Hash_Chain = libghdl.vhdl__nodes__set_hash_chain

Get_Design_Unit_Source_Pos = libghdl.vhdl__nodes__get_design_unit_source_pos

Set_Design_Unit_Source_Pos = libghdl.vhdl__nodes__set_design_unit_source_pos

Get_Design_Unit_Source_Line = libghdl.vhdl__nodes__get_design_unit_source_line

Set_Design_Unit_Source_Line = libghdl.vhdl__nodes__set_design_unit_source_line

Get_Design_Unit_Source_Col = libghdl.vhdl__nodes__get_design_unit_source_col

Set_Design_Unit_Source_Col = libghdl.vhdl__nodes__set_design_unit_source_col

Get_Value = libghdl.vhdl__nodes__get_value

Set_Value = libghdl.vhdl__nodes__set_value

Get_Enum_Pos = libghdl.vhdl__nodes__get_enum_pos

Set_Enum_Pos = libghdl.vhdl__nodes__set_enum_pos

Get_Physical_Literal = libghdl.vhdl__nodes__get_physical_literal

Set_Physical_Literal = libghdl.vhdl__nodes__set_physical_literal

Get_Fp_Value = libghdl.vhdl__nodes__get_fp_value

Set_Fp_Value = libghdl.vhdl__nodes__set_fp_value

Get_Simple_Aggregate_List = libghdl.vhdl__nodes__get_simple_aggregate_list

Set_Simple_Aggregate_List = libghdl.vhdl__nodes__set_simple_aggregate_list

Get_String8_Id = libghdl.vhdl__nodes__get_string8_id

Set_String8_Id = libghdl.vhdl__nodes__set_string8_id

Get_String_Length = libghdl.vhdl__nodes__get_string_length

Set_String_Length = libghdl.vhdl__nodes__set_string_length

Get_Bit_String_Base = libghdl.vhdl__nodes__get_bit_string_base

Set_Bit_String_Base = libghdl.vhdl__nodes__set_bit_string_base

Get_Has_Signed = libghdl.vhdl__nodes__get_has_signed

Set_Has_Signed = libghdl.vhdl__nodes__set_has_signed

Get_Has_Sign = libghdl.vhdl__nodes__get_has_sign

Set_Has_Sign = libghdl.vhdl__nodes__set_has_sign

Get_Has_Length = libghdl.vhdl__nodes__get_has_length

Set_Has_Length = libghdl.vhdl__nodes__set_has_length

Get_Literal_Length = libghdl.vhdl__nodes__get_literal_length

Set_Literal_Length = libghdl.vhdl__nodes__set_literal_length

Get_Literal_Origin = libghdl.vhdl__nodes__get_literal_origin

Set_Literal_Origin = libghdl.vhdl__nodes__set_literal_origin

Get_Range_Origin = libghdl.vhdl__nodes__get_range_origin

Set_Range_Origin = libghdl.vhdl__nodes__set_range_origin

Get_Literal_Subtype = libghdl.vhdl__nodes__get_literal_subtype

Set_Literal_Subtype = libghdl.vhdl__nodes__set_literal_subtype

Get_Allocator_Subtype = libghdl.vhdl__nodes__get_allocator_subtype

Set_Allocator_Subtype = libghdl.vhdl__nodes__set_allocator_subtype

Get_Entity_Class = libghdl.vhdl__nodes__get_entity_class

Set_Entity_Class = libghdl.vhdl__nodes__set_entity_class

Get_Entity_Name_List = libghdl.vhdl__nodes__get_entity_name_list

Set_Entity_Name_List = libghdl.vhdl__nodes__set_entity_name_list

Get_Attribute_Designator = libghdl.vhdl__nodes__get_attribute_designator

Set_Attribute_Designator = libghdl.vhdl__nodes__set_attribute_designator

Get_Attribute_Specification_Chain = libghdl.vhdl__nodes__get_attribute_specification_chain

Set_Attribute_Specification_Chain = libghdl.vhdl__nodes__set_attribute_specification_chain

Get_Attribute_Specification = libghdl.vhdl__nodes__get_attribute_specification

Set_Attribute_Specification = libghdl.vhdl__nodes__set_attribute_specification

Get_Signal_List = libghdl.vhdl__nodes__get_signal_list

Set_Signal_List = libghdl.vhdl__nodes__set_signal_list

Get_Designated_Entity = libghdl.vhdl__nodes__get_designated_entity

Set_Designated_Entity = libghdl.vhdl__nodes__set_designated_entity

Get_Formal = libghdl.vhdl__nodes__get_formal

Set_Formal = libghdl.vhdl__nodes__set_formal

Get_Actual = libghdl.vhdl__nodes__get_actual

Set_Actual = libghdl.vhdl__nodes__set_actual

Get_Actual_Conversion = libghdl.vhdl__nodes__get_actual_conversion

Set_Actual_Conversion = libghdl.vhdl__nodes__set_actual_conversion

Get_Formal_Conversion = libghdl.vhdl__nodes__get_formal_conversion

Set_Formal_Conversion = libghdl.vhdl__nodes__set_formal_conversion

Get_Whole_Association_Flag = libghdl.vhdl__nodes__get_whole_association_flag

Set_Whole_Association_Flag = libghdl.vhdl__nodes__set_whole_association_flag

Get_Collapse_Signal_Flag = libghdl.vhdl__nodes__get_collapse_signal_flag

Set_Collapse_Signal_Flag = libghdl.vhdl__nodes__set_collapse_signal_flag

Get_Artificial_Flag = libghdl.vhdl__nodes__get_artificial_flag

Set_Artificial_Flag = libghdl.vhdl__nodes__set_artificial_flag

Get_Open_Flag = libghdl.vhdl__nodes__get_open_flag

Set_Open_Flag = libghdl.vhdl__nodes__set_open_flag

Get_After_Drivers_Flag = libghdl.vhdl__nodes__get_after_drivers_flag

Set_After_Drivers_Flag = libghdl.vhdl__nodes__set_after_drivers_flag

Get_We_Value = libghdl.vhdl__nodes__get_we_value

Set_We_Value = libghdl.vhdl__nodes__set_we_value

Get_Time = libghdl.vhdl__nodes__get_time

Set_Time = libghdl.vhdl__nodes__set_time

Get_Associated_Expr = libghdl.vhdl__nodes__get_associated_expr

Set_Associated_Expr = libghdl.vhdl__nodes__set_associated_expr

Get_Associated_Block = libghdl.vhdl__nodes__get_associated_block

Set_Associated_Block = libghdl.vhdl__nodes__set_associated_block

Get_Associated_Chain = libghdl.vhdl__nodes__get_associated_chain

Set_Associated_Chain = libghdl.vhdl__nodes__set_associated_chain

Get_Choice_Name = libghdl.vhdl__nodes__get_choice_name

Set_Choice_Name = libghdl.vhdl__nodes__set_choice_name

Get_Choice_Expression = libghdl.vhdl__nodes__get_choice_expression

Set_Choice_Expression = libghdl.vhdl__nodes__set_choice_expression

Get_Choice_Range = libghdl.vhdl__nodes__get_choice_range

Set_Choice_Range = libghdl.vhdl__nodes__set_choice_range

Get_Same_Alternative_Flag = libghdl.vhdl__nodes__get_same_alternative_flag

Set_Same_Alternative_Flag = libghdl.vhdl__nodes__set_same_alternative_flag

Get_Element_Type_Flag = libghdl.vhdl__nodes__get_element_type_flag

Set_Element_Type_Flag = libghdl.vhdl__nodes__set_element_type_flag

Get_Architecture = libghdl.vhdl__nodes__get_architecture

Set_Architecture = libghdl.vhdl__nodes__set_architecture

Get_Block_Specification = libghdl.vhdl__nodes__get_block_specification

Set_Block_Specification = libghdl.vhdl__nodes__set_block_specification

Get_Prev_Block_Configuration = libghdl.vhdl__nodes__get_prev_block_configuration

Set_Prev_Block_Configuration = libghdl.vhdl__nodes__set_prev_block_configuration

Get_Configuration_Item_Chain = libghdl.vhdl__nodes__get_configuration_item_chain

Set_Configuration_Item_Chain = libghdl.vhdl__nodes__set_configuration_item_chain

Get_Attribute_Value_Chain = libghdl.vhdl__nodes__get_attribute_value_chain

Set_Attribute_Value_Chain = libghdl.vhdl__nodes__set_attribute_value_chain

Get_Spec_Chain = libghdl.vhdl__nodes__get_spec_chain

Set_Spec_Chain = libghdl.vhdl__nodes__set_spec_chain

Get_Value_Chain = libghdl.vhdl__nodes__get_value_chain

Set_Value_Chain = libghdl.vhdl__nodes__set_value_chain

Get_Attribute_Value_Spec_Chain = libghdl.vhdl__nodes__get_attribute_value_spec_chain

Set_Attribute_Value_Spec_Chain = libghdl.vhdl__nodes__set_attribute_value_spec_chain

Get_Entity_Name = libghdl.vhdl__nodes__get_entity_name

Set_Entity_Name = libghdl.vhdl__nodes__set_entity_name

Get_Package = libghdl.vhdl__nodes__get_package

Set_Package = libghdl.vhdl__nodes__set_package

Get_Package_Body = libghdl.vhdl__nodes__get_package_body

Set_Package_Body = libghdl.vhdl__nodes__set_package_body

Get_Instance_Package_Body = libghdl.vhdl__nodes__get_instance_package_body

Set_Instance_Package_Body = libghdl.vhdl__nodes__set_instance_package_body

Get_Need_Body = libghdl.vhdl__nodes__get_need_body

Set_Need_Body = libghdl.vhdl__nodes__set_need_body

Get_Macro_Expanded_Flag = libghdl.vhdl__nodes__get_macro_expanded_flag

Set_Macro_Expanded_Flag = libghdl.vhdl__nodes__set_macro_expanded_flag

Get_Need_Instance_Bodies = libghdl.vhdl__nodes__get_need_instance_bodies

Set_Need_Instance_Bodies = libghdl.vhdl__nodes__set_need_instance_bodies

Get_Hierarchical_Name = libghdl.vhdl__nodes__get_hierarchical_name

Set_Hierarchical_Name = libghdl.vhdl__nodes__set_hierarchical_name

Get_Inherit_Spec_Chain = libghdl.vhdl__nodes__get_inherit_spec_chain

Set_Inherit_Spec_Chain = libghdl.vhdl__nodes__set_inherit_spec_chain

Get_Vunit_Item_Chain = libghdl.vhdl__nodes__get_vunit_item_chain

Set_Vunit_Item_Chain = libghdl.vhdl__nodes__set_vunit_item_chain

Get_Bound_Vunit_Chain = libghdl.vhdl__nodes__get_bound_vunit_chain

Set_Bound_Vunit_Chain = libghdl.vhdl__nodes__set_bound_vunit_chain

Get_Block_Configuration = libghdl.vhdl__nodes__get_block_configuration

Set_Block_Configuration = libghdl.vhdl__nodes__set_block_configuration

Get_Concurrent_Statement_Chain = libghdl.vhdl__nodes__get_concurrent_statement_chain

Set_Concurrent_Statement_Chain = libghdl.vhdl__nodes__set_concurrent_statement_chain

Get_Chain = libghdl.vhdl__nodes__get_chain

Set_Chain = libghdl.vhdl__nodes__set_chain

Get_Port_Chain = libghdl.vhdl__nodes__get_port_chain

Set_Port_Chain = libghdl.vhdl__nodes__set_port_chain

Get_Generic_Chain = libghdl.vhdl__nodes__get_generic_chain

Set_Generic_Chain = libghdl.vhdl__nodes__set_generic_chain

Get_Type = libghdl.vhdl__nodes__get_type

Set_Type = libghdl.vhdl__nodes__set_type

Get_Subtype_Indication = libghdl.vhdl__nodes__get_subtype_indication

Set_Subtype_Indication = libghdl.vhdl__nodes__set_subtype_indication

Get_Discrete_Range = libghdl.vhdl__nodes__get_discrete_range

Set_Discrete_Range = libghdl.vhdl__nodes__set_discrete_range

Get_Type_Definition = libghdl.vhdl__nodes__get_type_definition

Set_Type_Definition = libghdl.vhdl__nodes__set_type_definition

Get_Subtype_Definition = libghdl.vhdl__nodes__get_subtype_definition

Set_Subtype_Definition = libghdl.vhdl__nodes__set_subtype_definition

Get_Incomplete_Type_Declaration = libghdl.vhdl__nodes__get_incomplete_type_declaration

Set_Incomplete_Type_Declaration = libghdl.vhdl__nodes__set_incomplete_type_declaration

Get_Interface_Type_Subprograms = libghdl.vhdl__nodes__get_interface_type_subprograms

Set_Interface_Type_Subprograms = libghdl.vhdl__nodes__set_interface_type_subprograms

Get_Nature = libghdl.vhdl__nodes__get_nature

Set_Nature = libghdl.vhdl__nodes__set_nature

Get_Mode = libghdl.vhdl__nodes__get_mode

Set_Mode = libghdl.vhdl__nodes__set_mode

Get_Guarded_Signal_Flag = libghdl.vhdl__nodes__get_guarded_signal_flag

Set_Guarded_Signal_Flag = libghdl.vhdl__nodes__set_guarded_signal_flag

Get_Signal_Kind = libghdl.vhdl__nodes__get_signal_kind

Set_Signal_Kind = libghdl.vhdl__nodes__set_signal_kind

Get_Base_Name = libghdl.vhdl__nodes__get_base_name

Set_Base_Name = libghdl.vhdl__nodes__set_base_name

Get_Interface_Declaration_Chain = libghdl.vhdl__nodes__get_interface_declaration_chain

Set_Interface_Declaration_Chain = libghdl.vhdl__nodes__set_interface_declaration_chain

Get_Subprogram_Specification = libghdl.vhdl__nodes__get_subprogram_specification

Set_Subprogram_Specification = libghdl.vhdl__nodes__set_subprogram_specification

Get_Sequential_Statement_Chain = libghdl.vhdl__nodes__get_sequential_statement_chain

Set_Sequential_Statement_Chain = libghdl.vhdl__nodes__set_sequential_statement_chain

Get_Subprogram_Body = libghdl.vhdl__nodes__get_subprogram_body

Set_Subprogram_Body = libghdl.vhdl__nodes__set_subprogram_body

Get_Overload_Number = libghdl.vhdl__nodes__get_overload_number

Set_Overload_Number = libghdl.vhdl__nodes__set_overload_number

Get_Subprogram_Depth = libghdl.vhdl__nodes__get_subprogram_depth

Set_Subprogram_Depth = libghdl.vhdl__nodes__set_subprogram_depth

Get_Subprogram_Hash = libghdl.vhdl__nodes__get_subprogram_hash

Set_Subprogram_Hash = libghdl.vhdl__nodes__set_subprogram_hash

Get_Impure_Depth = libghdl.vhdl__nodes__get_impure_depth

Set_Impure_Depth = libghdl.vhdl__nodes__set_impure_depth

Get_Return_Type = libghdl.vhdl__nodes__get_return_type

Set_Return_Type = libghdl.vhdl__nodes__set_return_type

Get_Implicit_Definition = libghdl.vhdl__nodes__get_implicit_definition

Set_Implicit_Definition = libghdl.vhdl__nodes__set_implicit_definition

Get_Default_Value = libghdl.vhdl__nodes__get_default_value

Set_Default_Value = libghdl.vhdl__nodes__set_default_value

Get_Deferred_Declaration = libghdl.vhdl__nodes__get_deferred_declaration

Set_Deferred_Declaration = libghdl.vhdl__nodes__set_deferred_declaration

Get_Deferred_Declaration_Flag = libghdl.vhdl__nodes__get_deferred_declaration_flag

Set_Deferred_Declaration_Flag = libghdl.vhdl__nodes__set_deferred_declaration_flag

Get_Shared_Flag = libghdl.vhdl__nodes__get_shared_flag

Set_Shared_Flag = libghdl.vhdl__nodes__set_shared_flag

Get_Design_Unit = libghdl.vhdl__nodes__get_design_unit

Set_Design_Unit = libghdl.vhdl__nodes__set_design_unit

Get_Block_Statement = libghdl.vhdl__nodes__get_block_statement

Set_Block_Statement = libghdl.vhdl__nodes__set_block_statement

Get_Signal_Driver = libghdl.vhdl__nodes__get_signal_driver

Set_Signal_Driver = libghdl.vhdl__nodes__set_signal_driver

Get_Declaration_Chain = libghdl.vhdl__nodes__get_declaration_chain

Set_Declaration_Chain = libghdl.vhdl__nodes__set_declaration_chain

Get_File_Logical_Name = libghdl.vhdl__nodes__get_file_logical_name

Set_File_Logical_Name = libghdl.vhdl__nodes__set_file_logical_name

Get_File_Open_Kind = libghdl.vhdl__nodes__get_file_open_kind

Set_File_Open_Kind = libghdl.vhdl__nodes__set_file_open_kind

Get_Element_Position = libghdl.vhdl__nodes__get_element_position

Set_Element_Position = libghdl.vhdl__nodes__set_element_position

Get_Use_Clause_Chain = libghdl.vhdl__nodes__get_use_clause_chain

Set_Use_Clause_Chain = libghdl.vhdl__nodes__set_use_clause_chain

Get_Context_Reference_Chain = libghdl.vhdl__nodes__get_context_reference_chain

Set_Context_Reference_Chain = libghdl.vhdl__nodes__set_context_reference_chain

Get_Selected_Name = libghdl.vhdl__nodes__get_selected_name

Set_Selected_Name = libghdl.vhdl__nodes__set_selected_name

Get_Type_Declarator = libghdl.vhdl__nodes__get_type_declarator

Set_Type_Declarator = libghdl.vhdl__nodes__set_type_declarator

Get_Complete_Type_Definition = libghdl.vhdl__nodes__get_complete_type_definition

Set_Complete_Type_Definition = libghdl.vhdl__nodes__set_complete_type_definition

Get_Incomplete_Type_Ref_Chain = libghdl.vhdl__nodes__get_incomplete_type_ref_chain

Set_Incomplete_Type_Ref_Chain = libghdl.vhdl__nodes__set_incomplete_type_ref_chain

Get_Associated_Type = libghdl.vhdl__nodes__get_associated_type

Set_Associated_Type = libghdl.vhdl__nodes__set_associated_type

Get_Enumeration_Literal_List = libghdl.vhdl__nodes__get_enumeration_literal_list

Set_Enumeration_Literal_List = libghdl.vhdl__nodes__set_enumeration_literal_list

Get_Entity_Class_Entry_Chain = libghdl.vhdl__nodes__get_entity_class_entry_chain

Set_Entity_Class_Entry_Chain = libghdl.vhdl__nodes__set_entity_class_entry_chain

Get_Group_Constituent_List = libghdl.vhdl__nodes__get_group_constituent_list

Set_Group_Constituent_List = libghdl.vhdl__nodes__set_group_constituent_list

Get_Unit_Chain = libghdl.vhdl__nodes__get_unit_chain

Set_Unit_Chain = libghdl.vhdl__nodes__set_unit_chain

Get_Primary_Unit = libghdl.vhdl__nodes__get_primary_unit

Set_Primary_Unit = libghdl.vhdl__nodes__set_primary_unit

Get_Identifier = libghdl.vhdl__nodes__get_identifier

Set_Identifier = libghdl.vhdl__nodes__set_identifier

Get_Label = libghdl.vhdl__nodes__get_label

Set_Label = libghdl.vhdl__nodes__set_label

Get_Visible_Flag = libghdl.vhdl__nodes__get_visible_flag

Set_Visible_Flag = libghdl.vhdl__nodes__set_visible_flag

Get_Range_Constraint = libghdl.vhdl__nodes__get_range_constraint

Set_Range_Constraint = libghdl.vhdl__nodes__set_range_constraint

Get_Direction = libghdl.vhdl__nodes__get_direction

Set_Direction = libghdl.vhdl__nodes__set_direction

Get_Left_Limit = libghdl.vhdl__nodes__get_left_limit

Set_Left_Limit = libghdl.vhdl__nodes__set_left_limit

Get_Right_Limit = libghdl.vhdl__nodes__get_right_limit

Set_Right_Limit = libghdl.vhdl__nodes__set_right_limit

Get_Left_Limit_Expr = libghdl.vhdl__nodes__get_left_limit_expr

Set_Left_Limit_Expr = libghdl.vhdl__nodes__set_left_limit_expr

Get_Right_Limit_Expr = libghdl.vhdl__nodes__get_right_limit_expr

Set_Right_Limit_Expr = libghdl.vhdl__nodes__set_right_limit_expr

Get_Base_Type = libghdl.vhdl__nodes__get_base_type

Set_Base_Type = libghdl.vhdl__nodes__set_base_type

Get_Resolution_Indication = libghdl.vhdl__nodes__get_resolution_indication

Set_Resolution_Indication = libghdl.vhdl__nodes__set_resolution_indication

Get_Record_Element_Resolution_Chain = libghdl.vhdl__nodes__get_record_element_resolution_chain

Set_Record_Element_Resolution_Chain = libghdl.vhdl__nodes__set_record_element_resolution_chain

Get_Tolerance = libghdl.vhdl__nodes__get_tolerance

Set_Tolerance = libghdl.vhdl__nodes__set_tolerance

Get_Plus_Terminal = libghdl.vhdl__nodes__get_plus_terminal

Set_Plus_Terminal = libghdl.vhdl__nodes__set_plus_terminal

Get_Minus_Terminal = libghdl.vhdl__nodes__get_minus_terminal

Set_Minus_Terminal = libghdl.vhdl__nodes__set_minus_terminal

Get_Simultaneous_Left = libghdl.vhdl__nodes__get_simultaneous_left

Set_Simultaneous_Left = libghdl.vhdl__nodes__set_simultaneous_left

Get_Simultaneous_Right = libghdl.vhdl__nodes__get_simultaneous_right

Set_Simultaneous_Right = libghdl.vhdl__nodes__set_simultaneous_right

Get_Text_File_Flag = libghdl.vhdl__nodes__get_text_file_flag

Set_Text_File_Flag = libghdl.vhdl__nodes__set_text_file_flag

Get_Only_Characters_Flag = libghdl.vhdl__nodes__get_only_characters_flag

Set_Only_Characters_Flag = libghdl.vhdl__nodes__set_only_characters_flag

Get_Is_Character_Type = libghdl.vhdl__nodes__get_is_character_type

Set_Is_Character_Type = libghdl.vhdl__nodes__set_is_character_type

Get_Type_Staticness = libghdl.vhdl__nodes__get_type_staticness

Set_Type_Staticness = libghdl.vhdl__nodes__set_type_staticness

Get_Constraint_State = libghdl.vhdl__nodes__get_constraint_state

Set_Constraint_State = libghdl.vhdl__nodes__set_constraint_state

Get_Index_Subtype_List = libghdl.vhdl__nodes__get_index_subtype_list

Set_Index_Subtype_List = libghdl.vhdl__nodes__set_index_subtype_list

Get_Index_Subtype_Definition_List = libghdl.vhdl__nodes__get_index_subtype_definition_list

Set_Index_Subtype_Definition_List = libghdl.vhdl__nodes__set_index_subtype_definition_list

Get_Element_Subtype_Indication = libghdl.vhdl__nodes__get_element_subtype_indication

Set_Element_Subtype_Indication = libghdl.vhdl__nodes__set_element_subtype_indication

Get_Element_Subtype = libghdl.vhdl__nodes__get_element_subtype

Set_Element_Subtype = libghdl.vhdl__nodes__set_element_subtype

Get_Index_Constraint_List = libghdl.vhdl__nodes__get_index_constraint_list

Set_Index_Constraint_List = libghdl.vhdl__nodes__set_index_constraint_list

Get_Array_Element_Constraint = libghdl.vhdl__nodes__get_array_element_constraint

Set_Array_Element_Constraint = libghdl.vhdl__nodes__set_array_element_constraint

Get_Elements_Declaration_List = libghdl.vhdl__nodes__get_elements_declaration_list

Set_Elements_Declaration_List = libghdl.vhdl__nodes__set_elements_declaration_list

Get_Owned_Elements_Chain = libghdl.vhdl__nodes__get_owned_elements_chain

Set_Owned_Elements_Chain = libghdl.vhdl__nodes__set_owned_elements_chain

Get_Designated_Type = libghdl.vhdl__nodes__get_designated_type

Set_Designated_Type = libghdl.vhdl__nodes__set_designated_type

Get_Designated_Subtype_Indication = libghdl.vhdl__nodes__get_designated_subtype_indication

Set_Designated_Subtype_Indication = libghdl.vhdl__nodes__set_designated_subtype_indication

Get_Index_List = libghdl.vhdl__nodes__get_index_list

Set_Index_List = libghdl.vhdl__nodes__set_index_list

Get_Reference = libghdl.vhdl__nodes__get_reference

Set_Reference = libghdl.vhdl__nodes__set_reference

Get_Nature_Declarator = libghdl.vhdl__nodes__get_nature_declarator

Set_Nature_Declarator = libghdl.vhdl__nodes__set_nature_declarator

Get_Across_Type = libghdl.vhdl__nodes__get_across_type

Set_Across_Type = libghdl.vhdl__nodes__set_across_type

Get_Through_Type = libghdl.vhdl__nodes__get_through_type

Set_Through_Type = libghdl.vhdl__nodes__set_through_type

Get_Target = libghdl.vhdl__nodes__get_target

Set_Target = libghdl.vhdl__nodes__set_target

Get_Waveform_Chain = libghdl.vhdl__nodes__get_waveform_chain

Set_Waveform_Chain = libghdl.vhdl__nodes__set_waveform_chain

Get_Guard = libghdl.vhdl__nodes__get_guard

Set_Guard = libghdl.vhdl__nodes__set_guard

Get_Delay_Mechanism = libghdl.vhdl__nodes__get_delay_mechanism

Set_Delay_Mechanism = libghdl.vhdl__nodes__set_delay_mechanism

Get_Reject_Time_Expression = libghdl.vhdl__nodes__get_reject_time_expression

Set_Reject_Time_Expression = libghdl.vhdl__nodes__set_reject_time_expression

Get_Sensitivity_List = libghdl.vhdl__nodes__get_sensitivity_list

Set_Sensitivity_List = libghdl.vhdl__nodes__set_sensitivity_list

Get_Process_Origin = libghdl.vhdl__nodes__get_process_origin

Set_Process_Origin = libghdl.vhdl__nodes__set_process_origin

Get_Package_Origin = libghdl.vhdl__nodes__get_package_origin

Set_Package_Origin = libghdl.vhdl__nodes__set_package_origin

Get_Condition_Clause = libghdl.vhdl__nodes__get_condition_clause

Set_Condition_Clause = libghdl.vhdl__nodes__set_condition_clause

Get_Timeout_Clause = libghdl.vhdl__nodes__get_timeout_clause

Set_Timeout_Clause = libghdl.vhdl__nodes__set_timeout_clause

Get_Postponed_Flag = libghdl.vhdl__nodes__get_postponed_flag

Set_Postponed_Flag = libghdl.vhdl__nodes__set_postponed_flag

Get_Callees_List = libghdl.vhdl__nodes__get_callees_list

Set_Callees_List = libghdl.vhdl__nodes__set_callees_list

Get_Passive_Flag = libghdl.vhdl__nodes__get_passive_flag

Set_Passive_Flag = libghdl.vhdl__nodes__set_passive_flag

Get_Resolution_Function_Flag = libghdl.vhdl__nodes__get_resolution_function_flag

Set_Resolution_Function_Flag = libghdl.vhdl__nodes__set_resolution_function_flag

Get_Wait_State = libghdl.vhdl__nodes__get_wait_state

Set_Wait_State = libghdl.vhdl__nodes__set_wait_state

Get_All_Sensitized_State = libghdl.vhdl__nodes__get_all_sensitized_state

Set_All_Sensitized_State = libghdl.vhdl__nodes__set_all_sensitized_state

Get_Seen_Flag = libghdl.vhdl__nodes__get_seen_flag

Set_Seen_Flag = libghdl.vhdl__nodes__set_seen_flag

Get_Pure_Flag = libghdl.vhdl__nodes__get_pure_flag

Set_Pure_Flag = libghdl.vhdl__nodes__set_pure_flag

Get_Foreign_Flag = libghdl.vhdl__nodes__get_foreign_flag

Set_Foreign_Flag = libghdl.vhdl__nodes__set_foreign_flag

Get_Resolved_Flag = libghdl.vhdl__nodes__get_resolved_flag

Set_Resolved_Flag = libghdl.vhdl__nodes__set_resolved_flag

Get_Signal_Type_Flag = libghdl.vhdl__nodes__get_signal_type_flag

Set_Signal_Type_Flag = libghdl.vhdl__nodes__set_signal_type_flag

Get_Has_Signal_Flag = libghdl.vhdl__nodes__get_has_signal_flag

Set_Has_Signal_Flag = libghdl.vhdl__nodes__set_has_signal_flag

Get_Purity_State = libghdl.vhdl__nodes__get_purity_state

Set_Purity_State = libghdl.vhdl__nodes__set_purity_state

Get_Elab_Flag = libghdl.vhdl__nodes__get_elab_flag

Set_Elab_Flag = libghdl.vhdl__nodes__set_elab_flag

Get_Configuration_Mark_Flag = libghdl.vhdl__nodes__get_configuration_mark_flag

Set_Configuration_Mark_Flag = libghdl.vhdl__nodes__set_configuration_mark_flag

Get_Configuration_Done_Flag = libghdl.vhdl__nodes__get_configuration_done_flag

Set_Configuration_Done_Flag = libghdl.vhdl__nodes__set_configuration_done_flag

Get_Index_Constraint_Flag = libghdl.vhdl__nodes__get_index_constraint_flag

Set_Index_Constraint_Flag = libghdl.vhdl__nodes__set_index_constraint_flag

Get_Hide_Implicit_Flag = libghdl.vhdl__nodes__get_hide_implicit_flag

Set_Hide_Implicit_Flag = libghdl.vhdl__nodes__set_hide_implicit_flag

Get_Assertion_Condition = libghdl.vhdl__nodes__get_assertion_condition

Set_Assertion_Condition = libghdl.vhdl__nodes__set_assertion_condition

Get_Report_Expression = libghdl.vhdl__nodes__get_report_expression

Set_Report_Expression = libghdl.vhdl__nodes__set_report_expression

Get_Severity_Expression = libghdl.vhdl__nodes__get_severity_expression

Set_Severity_Expression = libghdl.vhdl__nodes__set_severity_expression

Get_Instantiated_Unit = libghdl.vhdl__nodes__get_instantiated_unit

Set_Instantiated_Unit = libghdl.vhdl__nodes__set_instantiated_unit

Get_Generic_Map_Aspect_Chain = libghdl.vhdl__nodes__get_generic_map_aspect_chain

Set_Generic_Map_Aspect_Chain = libghdl.vhdl__nodes__set_generic_map_aspect_chain

Get_Port_Map_Aspect_Chain = libghdl.vhdl__nodes__get_port_map_aspect_chain

Set_Port_Map_Aspect_Chain = libghdl.vhdl__nodes__set_port_map_aspect_chain

Get_Configuration_Name = libghdl.vhdl__nodes__get_configuration_name

Set_Configuration_Name = libghdl.vhdl__nodes__set_configuration_name

Get_Component_Configuration = libghdl.vhdl__nodes__get_component_configuration

Set_Component_Configuration = libghdl.vhdl__nodes__set_component_configuration

Get_Configuration_Specification = libghdl.vhdl__nodes__get_configuration_specification

Set_Configuration_Specification = libghdl.vhdl__nodes__set_configuration_specification

Get_Default_Binding_Indication = libghdl.vhdl__nodes__get_default_binding_indication

Set_Default_Binding_Indication = libghdl.vhdl__nodes__set_default_binding_indication

Get_Default_Configuration_Declaration = libghdl.vhdl__nodes__get_default_configuration_declaration

Set_Default_Configuration_Declaration = libghdl.vhdl__nodes__set_default_configuration_declaration

Get_Expression = libghdl.vhdl__nodes__get_expression

Set_Expression = libghdl.vhdl__nodes__set_expression

Get_Conditional_Expression = libghdl.vhdl__nodes__get_conditional_expression

Set_Conditional_Expression = libghdl.vhdl__nodes__set_conditional_expression

Get_Allocator_Designated_Type = libghdl.vhdl__nodes__get_allocator_designated_type

Set_Allocator_Designated_Type = libghdl.vhdl__nodes__set_allocator_designated_type

Get_Selected_Waveform_Chain = libghdl.vhdl__nodes__get_selected_waveform_chain

Set_Selected_Waveform_Chain = libghdl.vhdl__nodes__set_selected_waveform_chain

Get_Conditional_Waveform_Chain = libghdl.vhdl__nodes__get_conditional_waveform_chain

Set_Conditional_Waveform_Chain = libghdl.vhdl__nodes__set_conditional_waveform_chain

Get_Guard_Expression = libghdl.vhdl__nodes__get_guard_expression

Set_Guard_Expression = libghdl.vhdl__nodes__set_guard_expression

Get_Guard_Decl = libghdl.vhdl__nodes__get_guard_decl

Set_Guard_Decl = libghdl.vhdl__nodes__set_guard_decl

Get_Guard_Sensitivity_List = libghdl.vhdl__nodes__get_guard_sensitivity_list

Set_Guard_Sensitivity_List = libghdl.vhdl__nodes__set_guard_sensitivity_list

Get_Signal_Attribute_Chain = libghdl.vhdl__nodes__get_signal_attribute_chain

Set_Signal_Attribute_Chain = libghdl.vhdl__nodes__set_signal_attribute_chain

Get_Block_Block_Configuration = libghdl.vhdl__nodes__get_block_block_configuration

Set_Block_Block_Configuration = libghdl.vhdl__nodes__set_block_block_configuration

Get_Package_Header = libghdl.vhdl__nodes__get_package_header

Set_Package_Header = libghdl.vhdl__nodes__set_package_header

Get_Block_Header = libghdl.vhdl__nodes__get_block_header

Set_Block_Header = libghdl.vhdl__nodes__set_block_header

Get_Uninstantiated_Package_Name = libghdl.vhdl__nodes__get_uninstantiated_package_name

Set_Uninstantiated_Package_Name = libghdl.vhdl__nodes__set_uninstantiated_package_name

Get_Uninstantiated_Package_Decl = libghdl.vhdl__nodes__get_uninstantiated_package_decl

Set_Uninstantiated_Package_Decl = libghdl.vhdl__nodes__set_uninstantiated_package_decl

Get_Instance_Source_File = libghdl.vhdl__nodes__get_instance_source_file

Set_Instance_Source_File = libghdl.vhdl__nodes__set_instance_source_file

Get_Generate_Block_Configuration = libghdl.vhdl__nodes__get_generate_block_configuration

Set_Generate_Block_Configuration = libghdl.vhdl__nodes__set_generate_block_configuration

Get_Generate_Statement_Body = libghdl.vhdl__nodes__get_generate_statement_body

Set_Generate_Statement_Body = libghdl.vhdl__nodes__set_generate_statement_body

Get_Alternative_Label = libghdl.vhdl__nodes__get_alternative_label

Set_Alternative_Label = libghdl.vhdl__nodes__set_alternative_label

Get_Generate_Else_Clause = libghdl.vhdl__nodes__get_generate_else_clause

Set_Generate_Else_Clause = libghdl.vhdl__nodes__set_generate_else_clause

Get_Condition = libghdl.vhdl__nodes__get_condition

Set_Condition = libghdl.vhdl__nodes__set_condition

Get_Else_Clause = libghdl.vhdl__nodes__get_else_clause

Set_Else_Clause = libghdl.vhdl__nodes__set_else_clause

Get_Parameter_Specification = libghdl.vhdl__nodes__get_parameter_specification

Set_Parameter_Specification = libghdl.vhdl__nodes__set_parameter_specification

Get_Parent = libghdl.vhdl__nodes__get_parent

Set_Parent = libghdl.vhdl__nodes__set_parent

Get_Loop_Label = libghdl.vhdl__nodes__get_loop_label

Set_Loop_Label = libghdl.vhdl__nodes__set_loop_label

Get_Component_Name = libghdl.vhdl__nodes__get_component_name

Set_Component_Name = libghdl.vhdl__nodes__set_component_name

Get_Instantiation_List = libghdl.vhdl__nodes__get_instantiation_list

Set_Instantiation_List = libghdl.vhdl__nodes__set_instantiation_list

Get_Entity_Aspect = libghdl.vhdl__nodes__get_entity_aspect

Set_Entity_Aspect = libghdl.vhdl__nodes__set_entity_aspect

Get_Default_Entity_Aspect = libghdl.vhdl__nodes__get_default_entity_aspect

Set_Default_Entity_Aspect = libghdl.vhdl__nodes__set_default_entity_aspect

Get_Binding_Indication = libghdl.vhdl__nodes__get_binding_indication

Set_Binding_Indication = libghdl.vhdl__nodes__set_binding_indication

Get_Named_Entity = libghdl.vhdl__nodes__get_named_entity

Set_Named_Entity = libghdl.vhdl__nodes__set_named_entity

Get_Alias_Declaration = libghdl.vhdl__nodes__get_alias_declaration

Set_Alias_Declaration = libghdl.vhdl__nodes__set_alias_declaration

Get_Referenced_Name = libghdl.vhdl__nodes__get_referenced_name

Set_Referenced_Name = libghdl.vhdl__nodes__set_referenced_name

Get_Expr_Staticness = libghdl.vhdl__nodes__get_expr_staticness

Set_Expr_Staticness = libghdl.vhdl__nodes__set_expr_staticness

Get_Error_Origin = libghdl.vhdl__nodes__get_error_origin

Set_Error_Origin = libghdl.vhdl__nodes__set_error_origin

Get_Operand = libghdl.vhdl__nodes__get_operand

Set_Operand = libghdl.vhdl__nodes__set_operand

Get_Left = libghdl.vhdl__nodes__get_left

Set_Left = libghdl.vhdl__nodes__set_left

Get_Right = libghdl.vhdl__nodes__get_right

Set_Right = libghdl.vhdl__nodes__set_right

Get_Unit_Name = libghdl.vhdl__nodes__get_unit_name

Set_Unit_Name = libghdl.vhdl__nodes__set_unit_name

Get_Name = libghdl.vhdl__nodes__get_name

Set_Name = libghdl.vhdl__nodes__set_name

Get_Group_Template_Name = libghdl.vhdl__nodes__get_group_template_name

Set_Group_Template_Name = libghdl.vhdl__nodes__set_group_template_name

Get_Name_Staticness = libghdl.vhdl__nodes__get_name_staticness

Set_Name_Staticness = libghdl.vhdl__nodes__set_name_staticness

Get_Prefix = libghdl.vhdl__nodes__get_prefix

Set_Prefix = libghdl.vhdl__nodes__set_prefix

Get_Signature_Prefix = libghdl.vhdl__nodes__get_signature_prefix

Set_Signature_Prefix = libghdl.vhdl__nodes__set_signature_prefix

Get_External_Pathname = libghdl.vhdl__nodes__get_external_pathname

Set_External_Pathname = libghdl.vhdl__nodes__set_external_pathname

Get_Pathname_Suffix = libghdl.vhdl__nodes__get_pathname_suffix

Set_Pathname_Suffix = libghdl.vhdl__nodes__set_pathname_suffix

Get_Pathname_Expression = libghdl.vhdl__nodes__get_pathname_expression

Set_Pathname_Expression = libghdl.vhdl__nodes__set_pathname_expression

Get_In_Formal_Flag = libghdl.vhdl__nodes__get_in_formal_flag

Set_In_Formal_Flag = libghdl.vhdl__nodes__set_in_formal_flag

Get_Slice_Subtype = libghdl.vhdl__nodes__get_slice_subtype

Set_Slice_Subtype = libghdl.vhdl__nodes__set_slice_subtype

Get_Suffix = libghdl.vhdl__nodes__get_suffix

Set_Suffix = libghdl.vhdl__nodes__set_suffix

Get_Index_Subtype = libghdl.vhdl__nodes__get_index_subtype

Set_Index_Subtype = libghdl.vhdl__nodes__set_index_subtype

Get_Parameter = libghdl.vhdl__nodes__get_parameter

Set_Parameter = libghdl.vhdl__nodes__set_parameter

Get_Attr_Chain = libghdl.vhdl__nodes__get_attr_chain

Set_Attr_Chain = libghdl.vhdl__nodes__set_attr_chain

Get_Signal_Attribute_Declaration = libghdl.vhdl__nodes__get_signal_attribute_declaration

Set_Signal_Attribute_Declaration = libghdl.vhdl__nodes__set_signal_attribute_declaration

Get_Actual_Type = libghdl.vhdl__nodes__get_actual_type

Set_Actual_Type = libghdl.vhdl__nodes__set_actual_type

Get_Actual_Type_Definition = libghdl.vhdl__nodes__get_actual_type_definition

Set_Actual_Type_Definition = libghdl.vhdl__nodes__set_actual_type_definition

Get_Association_Chain = libghdl.vhdl__nodes__get_association_chain

Set_Association_Chain = libghdl.vhdl__nodes__set_association_chain

Get_Individual_Association_Chain = libghdl.vhdl__nodes__get_individual_association_chain

Set_Individual_Association_Chain = libghdl.vhdl__nodes__set_individual_association_chain

Get_Subprogram_Association_Chain = libghdl.vhdl__nodes__get_subprogram_association_chain

Set_Subprogram_Association_Chain = libghdl.vhdl__nodes__set_subprogram_association_chain

Get_Aggregate_Info = libghdl.vhdl__nodes__get_aggregate_info

Set_Aggregate_Info = libghdl.vhdl__nodes__set_aggregate_info

Get_Sub_Aggregate_Info = libghdl.vhdl__nodes__get_sub_aggregate_info

Set_Sub_Aggregate_Info = libghdl.vhdl__nodes__set_sub_aggregate_info

Get_Aggr_Dynamic_Flag = libghdl.vhdl__nodes__get_aggr_dynamic_flag

Set_Aggr_Dynamic_Flag = libghdl.vhdl__nodes__set_aggr_dynamic_flag

Get_Aggr_Min_Length = libghdl.vhdl__nodes__get_aggr_min_length

Set_Aggr_Min_Length = libghdl.vhdl__nodes__set_aggr_min_length

Get_Aggr_Low_Limit = libghdl.vhdl__nodes__get_aggr_low_limit

Set_Aggr_Low_Limit = libghdl.vhdl__nodes__set_aggr_low_limit

Get_Aggr_High_Limit = libghdl.vhdl__nodes__get_aggr_high_limit

Set_Aggr_High_Limit = libghdl.vhdl__nodes__set_aggr_high_limit

Get_Aggr_Others_Flag = libghdl.vhdl__nodes__get_aggr_others_flag

Set_Aggr_Others_Flag = libghdl.vhdl__nodes__set_aggr_others_flag

Get_Aggr_Named_Flag = libghdl.vhdl__nodes__get_aggr_named_flag

Set_Aggr_Named_Flag = libghdl.vhdl__nodes__set_aggr_named_flag

Get_Aggregate_Expand_Flag = libghdl.vhdl__nodes__get_aggregate_expand_flag

Set_Aggregate_Expand_Flag = libghdl.vhdl__nodes__set_aggregate_expand_flag

Get_Association_Choices_Chain = libghdl.vhdl__nodes__get_association_choices_chain

Set_Association_Choices_Chain = libghdl.vhdl__nodes__set_association_choices_chain

Get_Case_Statement_Alternative_Chain = libghdl.vhdl__nodes__get_case_statement_alternative_chain

Set_Case_Statement_Alternative_Chain = libghdl.vhdl__nodes__set_case_statement_alternative_chain

Get_Choice_Staticness = libghdl.vhdl__nodes__get_choice_staticness

Set_Choice_Staticness = libghdl.vhdl__nodes__set_choice_staticness

Get_Procedure_Call = libghdl.vhdl__nodes__get_procedure_call

Set_Procedure_Call = libghdl.vhdl__nodes__set_procedure_call

Get_Implementation = libghdl.vhdl__nodes__get_implementation

Set_Implementation = libghdl.vhdl__nodes__set_implementation

Get_Parameter_Association_Chain = libghdl.vhdl__nodes__get_parameter_association_chain

Set_Parameter_Association_Chain = libghdl.vhdl__nodes__set_parameter_association_chain

Get_Method_Object = libghdl.vhdl__nodes__get_method_object

Set_Method_Object = libghdl.vhdl__nodes__set_method_object

Get_Subtype_Type_Mark = libghdl.vhdl__nodes__get_subtype_type_mark

Set_Subtype_Type_Mark = libghdl.vhdl__nodes__set_subtype_type_mark

Get_Type_Conversion_Subtype = libghdl.vhdl__nodes__get_type_conversion_subtype

Set_Type_Conversion_Subtype = libghdl.vhdl__nodes__set_type_conversion_subtype

Get_Type_Mark = libghdl.vhdl__nodes__get_type_mark

Set_Type_Mark = libghdl.vhdl__nodes__set_type_mark

Get_File_Type_Mark = libghdl.vhdl__nodes__get_file_type_mark

Set_File_Type_Mark = libghdl.vhdl__nodes__set_file_type_mark

Get_Return_Type_Mark = libghdl.vhdl__nodes__get_return_type_mark

Set_Return_Type_Mark = libghdl.vhdl__nodes__set_return_type_mark

Get_Has_Disconnect_Flag = libghdl.vhdl__nodes__get_has_disconnect_flag

Set_Has_Disconnect_Flag = libghdl.vhdl__nodes__set_has_disconnect_flag

Get_Has_Active_Flag = libghdl.vhdl__nodes__get_has_active_flag

Set_Has_Active_Flag = libghdl.vhdl__nodes__set_has_active_flag

Get_Is_Within_Flag = libghdl.vhdl__nodes__get_is_within_flag

Set_Is_Within_Flag = libghdl.vhdl__nodes__set_is_within_flag

Get_Type_Marks_List = libghdl.vhdl__nodes__get_type_marks_list

Set_Type_Marks_List = libghdl.vhdl__nodes__set_type_marks_list

Get_Implicit_Alias_Flag = libghdl.vhdl__nodes__get_implicit_alias_flag

Set_Implicit_Alias_Flag = libghdl.vhdl__nodes__set_implicit_alias_flag

Get_Alias_Signature = libghdl.vhdl__nodes__get_alias_signature

Set_Alias_Signature = libghdl.vhdl__nodes__set_alias_signature

Get_Attribute_Signature = libghdl.vhdl__nodes__get_attribute_signature

Set_Attribute_Signature = libghdl.vhdl__nodes__set_attribute_signature

Get_Overload_List = libghdl.vhdl__nodes__get_overload_list

Set_Overload_List = libghdl.vhdl__nodes__set_overload_list

Get_Simple_Name_Identifier = libghdl.vhdl__nodes__get_simple_name_identifier

Set_Simple_Name_Identifier = libghdl.vhdl__nodes__set_simple_name_identifier

Get_Simple_Name_Subtype = libghdl.vhdl__nodes__get_simple_name_subtype

Set_Simple_Name_Subtype = libghdl.vhdl__nodes__set_simple_name_subtype

Get_Protected_Type_Body = libghdl.vhdl__nodes__get_protected_type_body

Set_Protected_Type_Body = libghdl.vhdl__nodes__set_protected_type_body

Get_Protected_Type_Declaration = libghdl.vhdl__nodes__get_protected_type_declaration

Set_Protected_Type_Declaration = libghdl.vhdl__nodes__set_protected_type_declaration

Get_Use_Flag = libghdl.vhdl__nodes__get_use_flag

Set_Use_Flag = libghdl.vhdl__nodes__set_use_flag

Get_End_Has_Reserved_Id = libghdl.vhdl__nodes__get_end_has_reserved_id

Set_End_Has_Reserved_Id = libghdl.vhdl__nodes__set_end_has_reserved_id

Get_End_Has_Identifier = libghdl.vhdl__nodes__get_end_has_identifier

Set_End_Has_Identifier = libghdl.vhdl__nodes__set_end_has_identifier

Get_End_Has_Postponed = libghdl.vhdl__nodes__get_end_has_postponed

Set_End_Has_Postponed = libghdl.vhdl__nodes__set_end_has_postponed

Get_Has_Label = libghdl.vhdl__nodes__get_has_label

Set_Has_Label = libghdl.vhdl__nodes__set_has_label

Get_Has_Begin = libghdl.vhdl__nodes__get_has_begin

Set_Has_Begin = libghdl.vhdl__nodes__set_has_begin

Get_Has_End = libghdl.vhdl__nodes__get_has_end

Set_Has_End = libghdl.vhdl__nodes__set_has_end

Get_Has_Is = libghdl.vhdl__nodes__get_has_is

Set_Has_Is = libghdl.vhdl__nodes__set_has_is

Get_Has_Pure = libghdl.vhdl__nodes__get_has_pure

Set_Has_Pure = libghdl.vhdl__nodes__set_has_pure

Get_Has_Body = libghdl.vhdl__nodes__get_has_body

Set_Has_Body = libghdl.vhdl__nodes__set_has_body

Get_Has_Parameter = libghdl.vhdl__nodes__get_has_parameter

Set_Has_Parameter = libghdl.vhdl__nodes__set_has_parameter

Get_Has_Component = libghdl.vhdl__nodes__get_has_component

Set_Has_Component = libghdl.vhdl__nodes__set_has_component

Get_Has_Identifier_List = libghdl.vhdl__nodes__get_has_identifier_list

Set_Has_Identifier_List = libghdl.vhdl__nodes__set_has_identifier_list

Get_Has_Mode = libghdl.vhdl__nodes__get_has_mode

Set_Has_Mode = libghdl.vhdl__nodes__set_has_mode

Get_Has_Class = libghdl.vhdl__nodes__get_has_class

Set_Has_Class = libghdl.vhdl__nodes__set_has_class

Get_Suspend_Flag = libghdl.vhdl__nodes__get_suspend_flag

Set_Suspend_Flag = libghdl.vhdl__nodes__set_suspend_flag

Get_Is_Ref = libghdl.vhdl__nodes__get_is_ref

Set_Is_Ref = libghdl.vhdl__nodes__set_is_ref

Get_Is_Forward_Ref = libghdl.vhdl__nodes__get_is_forward_ref

Set_Is_Forward_Ref = libghdl.vhdl__nodes__set_is_forward_ref

Get_Psl_Property = libghdl.vhdl__nodes__get_psl_property

Set_Psl_Property = libghdl.vhdl__nodes__set_psl_property

Get_Psl_Sequence = libghdl.vhdl__nodes__get_psl_sequence

Set_Psl_Sequence = libghdl.vhdl__nodes__set_psl_sequence

Get_Psl_Declaration = libghdl.vhdl__nodes__get_psl_declaration

Set_Psl_Declaration = libghdl.vhdl__nodes__set_psl_declaration

Get_Psl_Expression = libghdl.vhdl__nodes__get_psl_expression

Set_Psl_Expression = libghdl.vhdl__nodes__set_psl_expression

Get_Psl_Boolean = libghdl.vhdl__nodes__get_psl_boolean

Set_Psl_Boolean = libghdl.vhdl__nodes__set_psl_boolean

Get_PSL_Clock = libghdl.vhdl__nodes__get_psl_clock

Set_PSL_Clock = libghdl.vhdl__nodes__set_psl_clock

Get_PSL_NFA = libghdl.vhdl__nodes__get_psl_nfa

Set_PSL_NFA = libghdl.vhdl__nodes__set_psl_nfa

Get_PSL_Nbr_States = libghdl.vhdl__nodes__get_psl_nbr_states

Set_PSL_Nbr_States = libghdl.vhdl__nodes__set_psl_nbr_states

Get_PSL_Clock_Sensitivity = libghdl.vhdl__nodes__get_psl_clock_sensitivity

Set_PSL_Clock_Sensitivity = libghdl.vhdl__nodes__set_psl_clock_sensitivity

Get_PSL_EOS_Flag = libghdl.vhdl__nodes__get_psl_eos_flag

Set_PSL_EOS_Flag = libghdl.vhdl__nodes__set_psl_eos_flag
