clc
close
clear

% Define the time range for the continuous signals
t = -3:0.01:3; % From -3 to 3 with a step of 0.01
% Define the unit step function
u = @(x) double(x >= 0); % u(t) = 1 for t >= 0, otherwise is 0

% Define g(t)
g1 = (t + 1) .* u(t + 1); % (t + 1)u(t + 1)
g2 = (t - 1) .* u(t - 1); % (t - 1)u(t - 1)
g3 = 2 .* u(t - 1); % 2u(t - 1)
g = g1 - g2 - g3; % g(t)

% Define h(t)
h1 = 2 .* u(t + 1); % 2u(t + 1)
h2 = 2 .* u(t); % -2u(t)
h3 = u(t - 1); % u(t - 1)
h4 = u(t - 2); % -u(t - 2)
h = h1 - h2 + h3 - h4; % h(t)

% Compute z(t)
z = g + h;
% Perform the convolution of g(t) and h(t)
% Scale the result to match the time step
y = conv(g, h, 'same') * (t(2) - t(1));
% Define the time vector for the convolution result
t_conv = t(1) + (0:length(y)-1) * (t(2) - t(1));

% Create the subplot figure
figure;
% Plot g(t)
subplot(2, 2, 1); % First subplot
plot(t, g, 'LineWidth', 1.5);
grid on;
xlabel('t');
ylabel('g');
title('g(t)');
% Plot h(t)
subplot(2, 2, 2); % Second subplot
plot(t, h, 'LineWidth', 1.5);
grid on;
xlabel('t');
ylabel('h');
title('h(t)');
% Plot z(t) = g(t) + h(t)
subplot(2, 2, 3); % Third subplot
plot(t, z, 'LineWidth', 1.5);
grid on;
xlabel('t');
ylabel('z');
title('z(t) = g(t) + h(t)');
% Plot y(t) = g(t) * h(t)
subplot(2, 2, 4); % Fourth subplot
plot(t_conv, y, 'LineWidth', 1.5);
grid on;
xlabel('t');
ylabel('y');
title('y(t) = g(t) * h(t)');