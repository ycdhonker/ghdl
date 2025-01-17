--  Values in synthesis.
--  Copyright (C) 2017 Tristan Gingold
--
--  This file is part of GHDL.
--
--  This program is free software; you can redistribute it and/or modify
--  it under the terms of the GNU General Public License as published by
--  the Free Software Foundation; either version 2 of the License, or
--  (at your option) any later version.
--
--  This program is distributed in the hope that it will be useful,
--  but WITHOUT ANY WARRANTY; without even the implied warranty of
--  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
--  GNU General Public License for more details.
--
--  You should have received a copy of the GNU General Public License
--  along with this program; if not, write to the Free Software
--  Foundation, Inc., 51 Franklin Street - Fifth Floor, Boston,
--  MA 02110-1301, USA.

with Types; use Types;
with Netlists; use Netlists;
with Vhdl.Nodes; use Vhdl.Nodes;
with Synth.Environment; use Synth.Environment;
with Areapools; use Areapools;


package Synth.Values is
   type Discrete_Range_Type is record
      --  An integer range.
      Dir : Iir_Direction;

      --  Netlist representation: signed or unsigned, width of vector.
      Is_Signed : Boolean;
      W : Width;

      Left : Int64;
      Right : Int64;
   end record;

   type Float_Range_Type is record
      Dir : Iir_Direction;
      Left : Fp64;
      Right : Fp64;
   end record;

   type Bound_Type is record
      Dir : Iir_Direction;
      Left : Int32;
      Right : Int32;
      Len : Width;

      --  Width of length.  This is the number of address bits.
      Wlen : Width;

      --  Width of bounds.  This is the precision used to compute the
      --  address.
      --  If bounds are 1 to 128 (so left = 1, dir = to, right = 128),
      --  Wlen = 7 and Wbounds = 8.
      Wbounds : Width;
   end record;

   type Bound_Array_Type is array (Iir_Index32 range <>) of Bound_Type;

   type Bound_Array (Len : Iir_Index32) is record
      D : Bound_Array_Type (1 .. Len);
   end record;

   type Bound_Array_Acc is access Bound_Array;

   type Type_Kind is
     (
      Type_Bit,
      Type_Discrete,
      Type_Float,
      Type_Vector,
      Type_Array,
      Type_Unbounded_Array,
      Type_Record
     );

   type Type_Type (Kind : Type_Kind);
   type Type_Acc is access Type_Type;

   type Type_Acc_Array_Type is array (Iir_Index32 range <>) of Type_Acc;

   type Type_Acc_Array (Len : Iir_Index32) is record
      E : Type_Acc_Array_Type (1 .. Len);
   end record;

   type Type_Acc_Array_Acc is access Type_Acc_Array;

   type Type_Type (Kind : Type_Kind) is record
      case Kind is
         when Type_Bit =>
            null;
         when Type_Discrete =>
            Drange : Discrete_Range_Type;
         when Type_Float =>
            Frange : Float_Range_Type;
         when Type_Vector =>
            Vbound : Bound_Type;
            Vec_El : Type_Acc;
         when Type_Array =>
            Abounds : Bound_Array_Acc;
            Arr_El : Type_Acc;
         when Type_Unbounded_Array =>
            Uarr_El : Type_Acc;
         when Type_Record =>
            Rec : Type_Acc_Array_Acc;
      end case;
   end record;

   --  Values is how signals and variables are decomposed.  This is similar to
   --  values in simulation, but simplified (no need to handle files,
   --  accesses...)

   type Value_Kind is
     (
      --  Value is for a vector or a bit, and is the output of a gate.
      Value_Net,

      --  Also a vector or a bit, but from an object.  Has to be transformed
      --  into a net.
      Value_Wire,

      Value_Mux2,

      --  A discrete value (integer or enumeration).
      Value_Discrete,

      Value_Float,

      --  An array.
      Value_Array,

      --  A record.
      Value_Record,

      --  A package.
      Value_Instance,

      --  A subtype.
      Value_Subtype
     );

   type Value_Type (Kind : Value_Kind);

   type Value_Acc is access Value_Type;

   type Value_Type_Array is array (Iir_Index32 range <>) of Value_Acc;

   type Value_Array_Type (Len : Iir_Index32) is record
      --  Values are from left to right.  So V(1) is at index 'Left.
      V : Value_Type_Array (1 .. Len);
   end record;

   type Value_Array_Acc is access Value_Array_Type;

   type Instance_Id is new Nat32;

   type Value_Type (Kind : Value_Kind) is record
      Typ : Type_Acc;
      case Kind is
         when Value_Net =>
            N : Net;
         when Value_Wire =>
            W : Wire_Id;
         when Value_Mux2 =>
            M_Cond : Value_Acc;
            M_T : Value_Acc;
            M_F : Value_Acc;
         when Value_Discrete =>
            Scal : Int64;
         when Value_Float =>
            Fp : Fp64;
         when Value_Subtype =>
            null;
         when Value_Array =>
            Arr : Value_Array_Acc;
         when Value_Record =>
            Rec : Value_Array_Acc;
         when Value_Instance =>
            Instance : Instance_Id;
      end case;
   end record;

   Global_Pool : aliased Areapool;
   Expr_Pool : aliased Areapool;

   --  Areapool used by Create_*_Value
   Current_Pool : Areapool_Acc := Expr_Pool'Access;

   --  Pool for objects allocated in the current instance.
   Instance_Pool : Areapool_Acc;

   --  Types.
   function Create_Discrete_Type (Rng : Discrete_Range_Type) return Type_Acc;
   function Create_Float_Type (Rng : Float_Range_Type) return Type_Acc;
   function Create_Vec_Type_By_Length (Len : Width; El : Type_Acc)
                                      return Type_Acc;
   function Create_Vector_Type (Bnd : Bound_Type; El_Type : Type_Acc)
                               return Type_Acc;
   function Create_Bound_Array (Ndims : Iir_Index32) return Bound_Array_Acc;
   function Create_Array_Type (Bnd : Bound_Array_Acc; El_Type : Type_Acc)
                              return Type_Acc;
   function Create_Unbounded_Array (El_Type : Type_Acc) return Type_Acc;

   --  Return the element of a vector/array/unbounded_array.
   function Get_Array_Element (Arr_Type : Type_Acc) return Type_Acc;

   function Is_Equal (L, R : Value_Acc) return Boolean;

   --  Create a Value_Net.
   function Create_Value_Net (N : Net; Ntype : Type_Acc) return Value_Acc;

   --  Create a Value_Wire.  For a bit wire, RNG must be null.
   function Create_Value_Wire (W : Wire_Id; Wtype : Type_Acc) return Value_Acc;

   --  Create a mux2.
   function Create_Value_Mux2 (Cond : Value_Acc; T : Value_Acc; F : Value_Acc)
                              return Value_Acc;

   function Create_Value_Discrete (Val : Int64; Vtype : Type_Acc)
                                  return Value_Acc;

   function Create_Value_Float (Val : Fp64; Vtype : Type_Acc) return Value_Acc;

   function Create_Value_Subtype (Typ : Type_Acc) return Value_Acc;

   function Create_Value_Array (Len : Iir_Index32) return Value_Array_Acc;

   --  Create a Value_Array.
   function Create_Value_Array (Bounds : Type_Acc; Arr : Value_Array_Acc)
                               return Value_Acc;

   --  Like the previous one but automatically build the array.
   function Create_Value_Array (Bounds : Type_Acc) return Value_Acc;

   --  Allocate the ARR component of the Value_Type ARR, using BOUNDS.
   procedure Create_Array_Data (Arr : Value_Acc);

   function Create_Value_Instance (Inst : Instance_Id) return Value_Acc;

   function Unshare (Src : Value_Acc; Pool : Areapool_Acc)
                    return Value_Acc;

   function Get_Type_Width (Atype : Type_Acc) return Width;

   procedure Init;

   --  Set by Init.
   Boolean_Type : Type_Acc := null;
   Logic_Type : Type_Acc := null;
   Bit_Type : Type_Acc := null;
end Synth.Values;
