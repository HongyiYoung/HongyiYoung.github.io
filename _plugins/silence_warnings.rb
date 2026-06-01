require 'active_support'

if ActiveSupport.respond_to?(:to_time_preserves_timezone=)
  ActiveSupport.to_time_preserves_timezone = :zone
end
