class Pascal
  def initialize()
  end

  def pascal(row, column)
    if row == column or row == 1
      return 1
    else
      val = pascal(row-1, column) + pascal(row-1, column-1)
      return val
    end
  end
end

if __FILE__ == $0
  p = Pascal.new
  puts(p.pascal(6, 4))
end
