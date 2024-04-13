"use client";

import { type ComponentProps } from "react";
type Props = ComponentProps<"button"> & {
  pendingText?: string;
  pending: boolean
};

export function SubmitButton({ children, pendingText, pending, ...props }: Props) {
  return (
    <button {...props} type="submit" aria-disabled={pending}>
      {pending ? pendingText : children}
    </button>
  );
}
